#!/usr/bin/env python3
"""Plot residual and force traces if solver log files are available."""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("log_file", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.log_file.exists():
        raise FileNotFoundError(args.log_file)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.text(0.5, 0.5, "Residual plotter is a planned post-processing hook.",
            ha="center", va="center")
    ax.set_axis_off()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=180)
    print(args.output)


if __name__ == "__main__":
    main()
