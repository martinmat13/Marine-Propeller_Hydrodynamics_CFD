#!/usr/bin/env python3
"""Compare CFD coefficients with a Wageningen B-series polynomial reference."""

import argparse
import csv
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cfd_csv", type=Path)
    parser.add_argument("reference_csv", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    with args.cfd_csv.open(newline="", encoding="utf-8") as handle:
        cfd = next(csv.DictReader(handle))
    cfd_J = float(cfd["J"])

    nearest = None
    with args.reference_csv.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            candidate = float(row["J"])
            if nearest is None or abs(candidate - cfd_J) < abs(float(nearest["J"]) - cfd_J):
                nearest = row
    if nearest is None:
        raise ValueError("Reference data is empty")

    def relative_error(observed, reference):
        reference = float(reference)
        return (float(observed) - reference) / reference * 100.0 if reference else float("nan")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["quantity", "CFD", "reference", "relative_error_percent"])
        for key, ref_key in (("KT", "KT"), ("10KQ", "10KQ"), ("eta0", "eta0")):
            observed = cfd[key]
            reference = nearest[ref_key]
            writer.writerow([key, observed, reference, relative_error(observed, reference)])
    print(args.output)


if __name__ == "__main__":
    main()
