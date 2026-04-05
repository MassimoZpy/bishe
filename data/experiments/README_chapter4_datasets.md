# Chapter 4 模型对应可用数据集（自动生成）

生成时间：2026-04-05（UTC）  
生成脚本：`scripts/generate_rq_datasets.py`

## 文件列表

1. `rq1_psm_did_panel.csv`：用于 PSM + DID 的 project-month 面板数据。  
2. `rq2_governance_index.csv`：用于 GTI 与 CEI 的治理机制数据。  
3. `rq3_fairness_distribution.csv`：用于集中度、V-F Gap 与分位数回归的数据。

## 字段说明

### RQ1（PSM + DID）
- `treat`：处理组虚拟变量。
- `post`：处理后时间虚拟变量（仅处理组在接入后为1）。
- `age_years_pre` / `activity_pre` / `star_growth_pre`：用于倾向得分估计的匹配前协变量。
- `matched_pair_id`：1:1 最近邻匹配后的配对ID。
- `new_sponsors` / `revenue_growth_rate`：可作为结果变量 $Y_{it}$。
- `contributors` / `release_freq`：可作为控制变量 $X_{it}$。

### RQ2（GTI / CEI）
- `gti = 0.35*ledger_public + 0.30*expense_trace + 0.20*budget_granularity + 0.15*update_freq_norm`
- `cei = 0.5*fiscal_host + 0.3*process_std + 0.2*rule_transparency`
- `sponsor_retention_rate`、`funding_volatility`：可作为“资助持续性”解释变量或被解释变量。

### RQ3（公平与分布）
- `criticality_rank_desc` 与 `funding_rank_desc`：分别为价值与资金排序。
- `vf_gap = criticality_rank_desc - funding_rank_desc`。
- `gini_funding_global` / `theil_funding_global`：整体资金分布集中度指标。
- `log_funding`：分位数回归常用变换后的因变量。

## 直接使用示例

```bash
python3 scripts/generate_rq_datasets.py
```

运行后即可在 `data/experiments/` 下得到 3 个可直接导入 R / Stata / Python 的 CSV 文件。
