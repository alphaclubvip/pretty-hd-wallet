import os
from mnemonic import Mnemonic
from bip44 import Wallet
from bip44.utils import get_eth_addr
from libs import fn

MIN_LENGTH = 3

while True:
    mnemonic = Mnemonic("english")
    words = mnemonic.generate(strength=256)

    w = Wallet(words)

    sk, pk = w.derive_account("eth", account=0)
    address = get_eth_addr(pk)
    raw = address[2:]
    start = fn.get_start(raw)
    end = fn.get_end(raw)

    p2f = None
    if len(start) > MIN_LENGTH and len(end) > MIN_LENGTH:
        p2f = os.path.join('./data', '{}__{}.txt'.format(start, end))
    if len(start) > MIN_LENGTH:
        p2f = os.path.join('./data', '{}__.txt'.format(start))
    if len(end) > MIN_LENGTH:
        p2f = os.path.join('./data', '__{}.txt'.format(end))

    if p2f:
        print(address)
        with open(p2f, 'w', encoding='utf-8') as f:
            f.write('{address} <= {sk} <= {words}'.format(address=address, sk=sk.hex(), words=words))
