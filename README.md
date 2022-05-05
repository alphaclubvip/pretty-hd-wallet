# Pretty HD Wallet

- 设定 `最小规律长度` / `钱包个数` / `CPU 线程数` 生成好看的 ETH 钱包地址
- 最高安全等级的 24 个助记词，可以导入硬钱包
- 由助记词推导私钥，私钥推导钱包地址
- 需要安装 `Python3` 环境
- 多线程
- 可以安全地脱机离线运行

## Install Python3

May be u should google it.

## Install dependencies and run the script

```bash
$ pip3 install mnemonic bip44
$ python main.py
> Min length: 4
> Wallets amount: 10
> Treads: 8
0xFEdCb76273c3b57f980D59941222A081252f18c7: ./data\FEDCB__.txt
0xd5e30b1Fa1fFB70711be7D382e5C1dC693fcAbCD: ./data\__ABCD.txt
0x614cBC9F1C4f9e6Ca6495600F70Bdfed8dB46666: ./data\__6666.txt
0x1d61223D0B88405a41Fee946F551eB2871d4AaAa: ./data\__AAAA.txt
0x3210831d0000AF5bb796081A3093A3Eeb606c0e8: ./data\3210__.txt
0x87654c997102b834a7a50610E401142Af6C0F13b: ./data\87654__.txt
0x1AB6E739353301aef3aCC8c854Ee8c502AdE8888: ./data\__8888.txt
0x43a62FB57F7B77a6c9C7e3A51053635eb1832222: ./data\__2222.txt
0x4444e579c5A6632D26BaA840df44850142Bb752f: ./data\4444__.txt
0x65439245138D7fdBf9479ee3dD7fc5c3B0a4D431: ./data\6543__.txt
```
