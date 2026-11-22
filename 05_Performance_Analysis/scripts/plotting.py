#!/usr/bin/env python3
"""Plot force and performance summaries without fabricating missing values."""

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cfd_csv", type=Path)
    parser.add_argument("reference_csv", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    with args.cfd_csv.open(newline="", encoding="utf-8") as handle:
        cfd_rows = list(csv.DictReader(handle))
    with args.reference_csv.open(newline="", encoding="utf-8") as handle:
        ref_rows = list(csv.DictReader(handle))

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    quantities = (("KT", "K_T"), ("10KQ", "10K_Q"), ("eta0", "eta_0"))
    for ax, (key, label) in zip(axes, quantities):
        ref_j = [float(row["J"]) for row in ref_rows]
        ref_y = [float(row[key]) for row in ref_rows]
        cfd_j = [float(row["J"]) for row in cfd_rows]
        cfd_y = [float(row[key]) for row in cfd_rows]
        ax.plot(ref_j, ref_y, "-", label="B-series polynomial")
        ax.plot(cfd_j, cfd_y, "o", label="CFD")
        ax.set_xlabel("J")
        ax.set_ylabel(label)
        ax.grid(True, alpha=0.3)
        ax.legend()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(args.output, dpi=180)
    print(args.output)


if __name__ == "__main__":
    main()
