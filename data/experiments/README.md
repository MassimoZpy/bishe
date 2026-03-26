# 论文实验数据集（按实验拆分）

本目录提供可直接作为论文实验输入的 3 份数据集，分别对应：

1. **实验1（平台采用效果）**：`exp1_platform_adoption_effect.csv`
2. **实验2（治理机制比较）**：`exp2_governance_mechanism_features.csv`
3. **实验3（公平与分配）**：`exp3_equity_and_distribution_metrics.csv`

此外，`dataset_index.csv` 由 `scripts/build_experiment_datasets.py` 自动生成，便于快速检查行数与用途。

## 字段与使用建议

- `source_url`：每条记录附带公开来源，便于溯源与论文引用。
- 实验1建议用于事件研究/叙述性比较，后续可继续追加 project-month 面板数据。
- 实验2可直接构造治理指标（如 GTI/CDI）的特征输入。
- 实验3可直接用于分配结构指标计算（如集中度、稳定性对比）。

## 复现

```bash
python3 scripts/build_experiment_datasets.py
```

运行后会更新：

- `data/experiments/dataset_index.csv`
