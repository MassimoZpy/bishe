# 论文实验数据集（按实验拆分）

本目录提供两类可直接作为论文实验输入的数据：

## A. 文献汇总型数据（既有）

1. **实验1（平台采用效果）**：`exp1_platform_adoption_effect.csv`
2. **实验2（治理机制比较）**：`exp2_governance_mechanism_features.csv`
3. **实验3（公平与分配）**：`exp3_equity_and_distribution_metrics.csv`

## B. 第4章模型直连数据（新增）

1. **RQ1 - PSM + DID 面板数据**：`rq1_psm_did_panel.csv`
2. **RQ2 - GTI/CEI 指数数据**：`rq2_governance_index.csv`
3. **RQ3 - 公平分布与错配数据**：`rq3_fairness_distribution.csv`
4. **字段字典与使用说明**：`README_chapter4_datasets.md`

此外，`dataset_index.csv` 由 `scripts/build_experiment_datasets.py` 自动生成，便于快速检查行数与用途。

## 快速复现

```bash
python3 scripts/generate_rq_datasets.py
python3 scripts/build_experiment_datasets.py
```

运行后会更新：

- `rq1_psm_did_panel.csv`
- `rq2_governance_index.csv`
- `rq3_fairness_distribution.csv`
- `README_chapter4_datasets.md`
- `dataset_index.csv`

## 使用建议

- 若要复现你在第4章中的模型，优先使用 `rq*.csv`。
- 若要写研究背景与对比分析，可继续使用 `exp*.csv`。
