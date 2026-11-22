#!/usr/bin/env python3
"""Generate a B-series regression reference curve for B5-75 P/D 1.20."""

import csv
from pathlib import Path

KT_FILE = Path(__file__).resolve().parent / "coefficients" / "kt.csv"
KQ_FILE = Path(__file__).resolve().parent / "coefficients" / "kq.csv"
OUTPUT = Path(__file__).resolve().parent.parent / "05_Performance_Analysis" / "reference_data" / "wageningen_b5_75_pd120.csv"


def read_terms(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return [
            (float(row["C"]), int(row["s"]), int(row["t"]), int(row["u"]), int(row["v"]))
            for row in csv.DictReader(handle)
        ]


def polynomial(terms, J, P_D, EAR, Z):
    return sum(c * J ** s * P_D ** t * EAR ** u * Z ** v for c, s, t, u, v in terms)


def main():
    if not KT_FILE.exists() or not KQ_FILE.exists():
        raise FileNotFoundError("Reference coefficient CSV files are missing")
    kt_terms = read_terms(KT_FILE)
    kq_terms = read_terms(KQ_FILE)
    P_D, EAR, Z = 1.20, 0.75, 5
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["J", "KT", "10KQ", "eta0", "source"])
        for J in [i / 20 for i in range(2, 25)]:
            kt = polynomial(kt_terms, J, P_D, EAR, Z)
            kq = polynomial(kq_terms, J, P_D, EAR, Z)
            eta = J / (2 * 3.141592653589793) * kt / kq if kq else float("nan")
            writer.writerow([f"{J:.3f}", f"{kt:.9e}", f"{10*kq:.9e}", f"{eta:.9e}",
                             "Oosterveld & van Oossanen 1975 Table 5"])
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
