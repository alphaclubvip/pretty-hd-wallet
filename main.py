from mnemonic import Mnemonic
from bip44 import Wallet
from bip44.utils import get_eth_addr

mnemonic = Mnemonic("english")
words = mnemonic.generate(strength=256)

w = Wallet(words)

sk, pk = w.derive_account("eth", account=0)
address = get_eth_addr(pk)

print(words)
print(address)
