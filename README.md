# pairwise-underwater-color-restore

## 领域

游戏、图形与多媒体

## 主题

水下图像颜色恢复

## 说明

深度相关衰减、散射区掩码、补光分区白平衡。

初始状态下 `imaging/underwater_color.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
