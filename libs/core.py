import os
import moment
from mnemonic import Mnemonic
from bip44 import Wallet
from bip44.utils import get_eth_addr

PREFIX_SUFFIX = 4


def confirm(s: str = ''):
    while True:
        value = input('> {} [y/n]: '.format(s)).lower()
        if value:
            if value in 'yes':
                return True
            elif value in 'no':
                return False


def raw(s: str = '', default: str = None):
    if default and confirm('Use {} = "{}":'.format(s, default)):
        return default

    while True:
        value = input('> {}: '.format(s))
        if value:
            return value


def integer(s: str = ''):
    value = None
    try:
        while True:
            value = int(raw(s))
            if value > 0:
                return value
            else:
                print('--- "{}" < 1'.format(value))
    except ValueError:
        print('"{}" is not a integer.'.format(value))
        return integer(s)


def get_start(s: str):
    same = None
    char = None
    text = ''

    for key, c in enumerate(s):
        i = int(c, 16)

        if key == 0:
            char = i
            text = c
        elif key == 1:
            if i == char and text.islower() == c.islower():
                same = 0
                text += c
            elif char + 1 == i and text.islower() == c.islower() and char < 10 and i < 10:
                same = 1
                char = i
                text += c
            elif char - 1 == i and text.islower() == c.islower() and char < 10 and i < 10:
                same = -1
                char = i
                text += c
            else:
                return same, text
        else:
            if same == 0 and char == i and text.islower() == c.islower():
                text += c
            elif same == 1 and char + 1 == i and text.islower() == c.islower() and i < 10:
                char = i
                text += c
            elif same == -1 and char - 1 == i and text.islower() == c.islower() and i < 10:
                char = i
                text += c
            else:
                return same, text

    return same, text


def get_end(s: str):
    return get_start(s[::-1])[::-1]


def generate(i, min_length: int = 4):
    while True:
        mnemonic = Mnemonic("english")
        words = mnemonic.generate(strength=256)

        w = Wallet(words)
        sk, pk = w.derive_account("eth", account=0)
        address = get_eth_addr(pk)
        line = address[2:]
        start_same, start_chars = get_start(line)
        end_same, end_chars = get_end(line)

        p2f = None
        pat = ''
        if start_same == 0 and end_same == 0 \
                and len(start_chars) >= int(min_length / 2) \
                and len(end_chars) >= int(min_length / 2):
            p2f = os.path.join('./data', '{}__{}.txt'.format(start_chars, end_chars))
            pat = '{}__{}.txt'.format(start_chars, end_chars)
        elif len(start_chars) >= PREFIX_SUFFIX and len(end_chars) >= PREFIX_SUFFIX and start_same == 0 - end_same:
            p2f = os.path.join('./data', '{}__{}.txt'.format(start_chars, end_chars))
            pat = '{}__{}.txt'.format(start_chars, end_chars)
        elif len(start_chars) >= min_length:
            p2f = os.path.join('./data', '{}__.txt'.format(start_chars))
            pat = '{}__.txt'.format(start_chars)
        elif len(end_chars) >= min_length:
            p2f = os.path.join('./data', '__{}.txt'.format(end_chars))
            pat = '__{}.txt'.format(end_chars)

        if p2f:
            with open(p2f, 'a', encoding='utf-8') as f:
                f.write('{address} <= {sk} <= {words}\n'.format(address=address, sk=sk.hex(), words=words))

            print('{} -- {} -- {}'.format(moment.now().format('YYYY-MM-DD HH:mm:ss'), address, pat))
            return address
