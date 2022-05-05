import os
from mnemonic import Mnemonic
from bip44 import Wallet
from bip44.utils import get_eth_addr


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
            if i == char:
                same = 0
                text += c
            elif char + 1 == i:
                same = 1
                char = i
                text += c
            elif char - 1 == i:
                same = -1
                char = i
                text += c
            else:
                return text.upper()
        else:
            if same == 0 and char == i:
                text += c
            elif same == 1 and char + 1 == i:
                char = i
                text += c
            elif same == -1 and char - 1 == i:
                char = i
                text += c
            else:
                return text.upper()

    return text.upper()


def get_end(s: str):
    s = s[::-1]
    same = None
    char = None
    text = ''

    for key, c in enumerate(s):
        i = int(c, 16)

        if key == 0:
            char = i
            text = c
        elif key == 1:
            if i == char:
                same = 0
                text += c
            elif char + 1 == i:
                same = -1
                char = i
                text += c
            elif char - 1 == i:
                same = 1
                char = i
                text += c
            else:
                return text[::-1].upper()
        else:
            if same == 0 and char == i:
                text += c
            elif same == 1 and char - 1 == i:
                char = i
                text += c
            elif same == -1 and char + 1 == i:
                char = i
                text += c
            else:
                return text[::-1].upper()

    return text[::-1].upper()


def generate(i, min_length: int = 4):
    while True:
        mnemonic = Mnemonic("english")
        words = mnemonic.generate(strength=256)

        w = Wallet(words)

        sk, pk = w.derive_account("eth", account=0)
        address = get_eth_addr(pk)
        line = address[2:]
        start = get_start(line)
        end = get_end(line)

        p2f = None
        if len(start) >= min_length and len(end) >= min_length:
            p2f = os.path.join('./data', '{}__{}.txt'.format(start, end))
        if len(start) >= min_length:
            p2f = os.path.join('./data', '{}__.txt'.format(start))
        if len(end) >= min_length:
            p2f = os.path.join('./data', '__{}.txt'.format(end))

        if p2f:
            with open(p2f, 'a', encoding='utf-8') as f:
                f.write('{address} <= {sk} <= {words}\n'.format(address=address, sk=sk.hex(), words=words))

            print('{}: {}'.format(address, p2f))
            return address
