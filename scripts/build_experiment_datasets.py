#!/usr/bin/env python3
"""Build an index for thesis experiment datasets."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "experiments"
INDEX_FILE = DATA_DIR / "dataset_index.csv"


def count_rows(csv_path: Path) -> int:
    with csv_path.open("r", encoding="utf-8") as f:
        return max(sum(1 for _ in f) - 1, 0)


def infer_purpose(file_name: str) -> str:
    if "exp1" in file_name or "rq1" in file_name:
        return "Experiment 1 / RQ1: PSM + DID platform adoption effect"
    if "exp2" in file_name or "rq2" in file_name:
        return "Experiment 2 / RQ2: governance transparency & compliance indices"
    if "exp3" in file_name or "rq3" in file_name:
        return "Experiment 3 / RQ3: fairness, concentration, and mismatch metrics"
    return "Other experiment-support dataset"


def main() -> None:
    files = sorted(p for p in DATA_DIR.glob("*.csv") if p.name != INDEX_FILE.name)
    with INDEX_FILE.open("w", encoding="utf-8", newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["dataset_file", "rows", "purpose"])
        for file in files:
            writer.writerow([file.name, count_rows(file), infer_purpose(file.name)])


if __name__ == "__main__":
    main()
