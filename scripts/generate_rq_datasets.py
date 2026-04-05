#!/usr/bin/env python3
"""Generate model-ready datasets for RQ1-RQ3 in Chapter 4.

The script creates synthetic but structurally faithful datasets that can be
used directly in econometric workflows:
- RQ1: PSM + DID project-month panel
- RQ2: Governance transparency/compliance indices (GTI/CEI)
- RQ3: Fairness distribution, concentration, and quantile-ready variables
"""

from __future__ import annotations

import csv
import math
import random
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data" / "experiments"

SEED = 20260405
random.seed(SEED)


def month_range(start_year: int, start_month: int, periods: int) -> list[str]:
    months: list[str] = []
    y, m = start_year, start_month
    for _ in range(periods):
        months.append(f"{y:04d}-{m:02d}")
        m += 1
        if m > 12:
            m = 1
            y += 1
    return months


def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def percentile_rank_desc(values: list[float]) -> list[int]:
    indexed = sorted(enumerate(values), key=lambda x: x[1], reverse=True)
    ranks = [0] * len(values)
    for r, (idx, _) in enumerate(indexed, start=1):
        ranks[idx] = r
    return ranks


def gini(values: list[float]) -> float:
    vals = sorted(max(v, 0.0) for v in values)
    n = len(vals)
    if n == 0:
        return 0.0
    s = sum(vals)
    if s == 0:
        return 0.0
    weighted = sum((i + 1) * v for i, v in enumerate(vals))
    return (2 * weighted) / (n * s) - (n + 1) / n


def theil(values: list[float]) -> float:
    vals = [max(v, 1e-9) for v in values]
    n = len(vals)
    if n == 0:
        return 0.0
    mean_v = sum(vals) / n
    return sum((v / mean_v) * math.log(v / mean_v) for v in vals) / n


def write_csv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def build_rq1_panel() -> None:
    """PSM + DID model-ready panel."""
    months = month_range(2024, 1, 24)
    n_projects = 220

    project_records: list[dict[str, object]] = []

    # Baseline covariates for propensity score
    for i in range(1, n_projects + 1):
        age = random.randint(1, 12)
        activity = round(random.uniform(2, 40), 2)
        star_growth = round(random.uniform(-0.08, 0.50), 3)

        z = -0.9 + 0.10 * age + 0.045 * activity + 2.2 * star_growth
        pscore = sigmoid(z)
        treat = 1 if random.random() < pscore else 0

        # adoption month for treated projects
        adoption_idx = random.randint(8, 16) if treat else -1
        project_records.append(
            {
                "project_id": f"P{i:04d}",
                "age_years": age,
                "activity_pre": activity,
                "star_growth_pre": star_growth,
                "propensity_score": round(pscore, 4),
                "treat": treat,
                "adoption_month": months[adoption_idx] if treat else "NA",
                "adoption_idx": adoption_idx,
            }
        )

    treated = [p for p in project_records if p["treat"] == 1]
    controls = [p for p in project_records if p["treat"] == 0]

    # 1:1 nearest-neighbor matching by propensity score
    available_controls = controls[:]
    matched_pairs: list[tuple[dict[str, object], dict[str, object], int]] = []
    pair_id = 1
    for t in sorted(treated, key=lambda x: x["propensity_score"]):
        if not available_controls:
            break
        best_idx = min(
            range(len(available_controls)),
            key=lambda j: abs(float(available_controls[j]["propensity_score"]) - float(t["propensity_score"])),
        )
        c = available_controls.pop(best_idx)
        matched_pairs.append((t, c, pair_id))
        pair_id += 1

    matched_projects = {p["project_id"]: pid for t, c, pid in matched_pairs for p in (t, c)}

    rows: list[list[object]] = []
    for p in project_records:
        if p["project_id"] not in matched_projects:
            continue
        pid = matched_projects[p["project_id"]]

        baseline_contrib = random.randint(2, 35)
        baseline_release = round(random.uniform(0.2, 2.4), 2)
        baseline_revenue = round(random.uniform(80, 3200), 2)

        for idx, month in enumerate(months):
            post = 1 if p["treat"] == 1 and idx >= int(p["adoption_idx"]) else 0

            trend = 0.8 * idx
            contrib = max(1, int(round(baseline_contrib + 0.25 * idx + random.gauss(0, 2))))
            release_freq = round(max(0.05, baseline_release + random.gauss(0, 0.2)), 2)

            # ATT embedded as post-treatment lift for treated projects
            sponsor_new = max(
                0,
                int(
                    round(
                        0.2
                        + 0.07 * contrib
                        + 1.3 * release_freq
                        + 4.2 * post
                        + trend * 0.05
                        + random.gauss(0, 1.5)
                    )
                ),
            )
            revenue_growth = round(
                0.005 * contrib + 0.018 * release_freq + 0.06 * post + random.gauss(0, 0.03),
                4,
            )
            monthly_revenue = round(max(0, baseline_revenue * (1 + revenue_growth)), 2)

            rows.append(
                [
                    p["project_id"],
                    month,
                    p["treat"],
                    post,
                    pid,
                    p["age_years"],
                    p["activity_pre"],
                    p["star_growth_pre"],
                    p["propensity_score"],
                    contrib,
                    release_freq,
                    sponsor_new,
                    revenue_growth,
                    monthly_revenue,
                ]
            )

    write_csv(
        OUT_DIR / "rq1_psm_did_panel.csv",
        [
            "project_id",
            "month",
            "treat",
            "post",
            "matched_pair_id",
            "age_years_pre",
            "activity_pre",
            "star_growth_pre",
            "propensity_score",
            "contributors",
            "release_freq",
            "new_sponsors",
            "revenue_growth_rate",
            "monthly_revenue_usd",
        ],
        rows,
    )


def build_rq2_governance() -> None:
    """Governance mechanism dataset with GTI/CEI."""
    n_projects = 220
    rows: list[list[object]] = []

    for i in range(1, n_projects + 1):
        project_id = f"P{i:04d}"
        ledger_public = random.choice([0, 1])
        expense_trace = random.choice([0, 1])
        budget_granularity = random.choice([0, 0.5, 1])
        update_freq = round(random.uniform(0.1, 1), 3)

        fiscal_host = random.choice([0, 1])
        process_std = random.choice([0, 0.5, 1])
        rule_transparency = random.choice([0, 0.5, 1])

        gti = round(
            0.35 * ledger_public
            + 0.30 * expense_trace
            + 0.20 * budget_granularity
            + 0.15 * update_freq,
            4,
        )
        cei = round(0.5 * fiscal_host + 0.3 * process_std + 0.2 * rule_transparency, 4)

        # proxy stability target (for downstream regression)
        sponsor_retention = round(min(1, max(0, 0.25 + 0.35 * gti + 0.30 * cei + random.gauss(0, 0.08))), 4)
        funding_volatility = round(max(0.01, 0.45 - 0.22 * gti - 0.18 * cei + random.gauss(0, 0.05)), 4)

        rows.append(
            [
                project_id,
                ledger_public,
                expense_trace,
                budget_granularity,
                update_freq,
                fiscal_host,
                process_std,
                rule_transparency,
                gti,
                cei,
                sponsor_retention,
                funding_volatility,
            ]
        )

    write_csv(
        OUT_DIR / "rq2_governance_index.csv",
        [
            "project_id",
            "ledger_public",
            "expense_trace",
            "budget_granularity",
            "update_freq_norm",
            "fiscal_host",
            "process_std",
            "rule_transparency",
            "gti",
            "cei",
            "sponsor_retention_rate",
            "funding_volatility",
        ],
        rows,
    )


def build_rq3_fairness() -> None:
    """Distribution/fairness dataset with concentration and V-F Gap."""
    n_projects = 220
    rows: list[list[object]] = []

    criticality = [max(0.001, random.lognormvariate(0.0, 0.75)) for _ in range(n_projects)]
    funding = []
    treat_flags = []
    for c in criticality:
        treat = 1 if random.random() < 0.48 else 0
        # Introduce Matthew effect: funding grows super-linearly with criticality + treat premium
        amount = 450 * (c ** 1.35) * (1 + 0.24 * treat) * random.uniform(0.55, 1.55)
        funding.append(round(amount, 2))
        treat_flags.append(treat)

    c_ranks = percentile_rank_desc(criticality)
    f_ranks = percentile_rank_desc(funding)

    gini_all = round(gini(funding), 4)
    theil_all = round(theil(funding), 4)

    for i in range(n_projects):
        gap = c_ranks[i] - f_ranks[i]
        ln_funding = round(math.log(max(funding[i], 1)), 5)

        rows.append(
            [
                f"P{i+1:04d}",
                treat_flags[i],
                round(criticality[i], 6),
                funding[i],
                c_ranks[i],
                f_ranks[i],
                gap,
                gini_all,
                theil_all,
                ln_funding,
            ]
        )

    write_csv(
        OUT_DIR / "rq3_fairness_distribution.csv",
        [
            "project_id",
            "treat",
            "criticality_score",
            "funding_usd",
            "criticality_rank_desc",
            "funding_rank_desc",
            "vf_gap",
            "gini_funding_global",
            "theil_funding_global",
            "log_funding",
        ],
        rows,
    )


def write_codebook() -> None:
    text = f"""# Chapter 4 模型对应可用数据集（自动生成）

生成时间：{date.today().isoformat()}（UTC）  
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
- `new_sponsors` / `revenue_growth_rate`：可作为结果变量 $Y_{{it}}$。
- `contributors` / `release_freq`：可作为控制变量 $X_{{it}}$。

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
"""
    (OUT_DIR / "README_chapter4_datasets.md").write_text(text, encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_rq1_panel()
    build_rq2_governance()
    build_rq3_fairness()
    write_codebook()


if __name__ == "__main__":
    main()
