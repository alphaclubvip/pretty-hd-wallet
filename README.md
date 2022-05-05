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
$ pip3 install moment mnemonic bip44
$ python main.py
> Min length: 6
> Wallets amount: 10
> Treads: 20
0xEbEE13F3eB0815D3364Ba1a670c7196526456789: ./data\__456789.txt
0x8A77bD4C8A19321105d109810E53BC546D888888: ./data\__888888.txt
0x9876541561F65Da16a4681E916C5bbaB47b12BBb: ./data\987654__.txt
0x3D16aa7729cf3c34492D425C2cE7C6488AEeEeEe: ./data\__EEEEEE.txt
0x89AbCdb6D9Fc2E8E0da18A4bF6f1ff5c1062B487: ./data\89ABCD__.txt
0x111111f147C73Ca04cfA23C928E02B7D3d1747f1: ./data\111111__.txt
0x7409949aBf12Ff502c715b8C49237b5096876543: ./data\__876543.txt
0x456789D341B9047AB6449FeDC608bb9700280247: ./data\456789__.txt
0x297008077056A23606b2d6F510f246D509012345: ./data\__012345.txt
0xBa9876Ef7129D47bE5e0353629AB75bEe71b2F5C: ./data\BA9876__.txt
```
