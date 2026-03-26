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


def main() -> None:
    files = sorted(p for p in DATA_DIR.glob("exp*.csv") if p.name != INDEX_FILE.name)
    with INDEX_FILE.open("w", encoding="utf-8", newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["dataset_file", "rows", "purpose"])
        for file in files:
            if "exp1" in file.name:
                purpose = "Experiment 1: platform adoption short/mid-term effect evidence"
            elif "exp2" in file.name:
                purpose = "Experiment 2: governance and mechanism comparison"
            else:
                purpose = "Experiment 3: equity/distribution metrics"
            writer.writerow([file.name, count_rows(file), purpose])


if __name__ == "__main__":
    main()
