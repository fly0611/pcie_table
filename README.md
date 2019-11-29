# 生成已插入Pci-E设备详情的字符表格
## **原理**
### 通过dmidecode 获取Pci-E设备的BUS address,在位信息，将其生成为字典
### 将其bus address 和lspc生成结果相对应，生成完整的pcie字典
### 将pcie设备字典用字符表格 格式化输出
## **效果如下：**
```
+--------------------------+-------------+---------------+--------+------------------------------------------------+------------------------+--------------+
|         SVendor          | Designation | Current Usage | Length |                     device                     |          Type          | Bus Address  |
+--------------------------+-------------+---------------+--------+------------------------------------------------+------------------------+--------------+
|           N/A            |  CPU2 SLOT7 |   Available   |  Long  |                      N/A                       |  x16 PCI Express 3 x16 | 0000:ff:00.0 |
|           N/A            |  CPU2 SLOT6 |   Available   |  Long  |                      N/A                       |  x16 PCI Express 3 x16 | 0000:ff:00.0 |
| Super Micro Computer Inc |  CPU2 SLOT5 |     In Use    |  Short | 82599ES 10-Gigabit SFI/SFP+ Network Connection |   x8 PCI Express 3 x8  | 0000:81:00.0 |
| Super Micro Computer Inc |  CPU2 SLOT4 |     In Use    |  Long  | 82599ES 10-Gigabit SFI/SFP+ Network Connection |  x16 PCI Express 3 x16 | 0000:82:00.0 |
|           N/A            |  CPU1 SLOT3 |   Available   |  Short |                      N/A                       |   x8 PCI Express 3 x8  | 0000:04:00.0 |
| Super Micro Computer Inc |  CPU1 SLOT2 |     In Use    |  Long  |      SAS3008 PCI-Express Fusion-MPT SAS-3      |  x16 PCI Express 3 x16 | 0000:03:00.0 |
|           N/A            |  CPU1 SLOT1 |   Available   |  Short |                      N/A                       |   x8 PCI Express 3 x8  | 0000:02:00.0 |
+--------------------------+-------------+---------------+--------+------------------------------------------------+------------------------+--------------+

```
`此代码为学习pyhon所写，仅供参考` 
