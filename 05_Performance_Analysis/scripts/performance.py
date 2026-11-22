#!/usr/bin/env python3
"""Calculate propeller open-water coefficients from force data."""

import argparse
import csv
from pathlib import Path

import numpy as np


def mean_tail(path: Path, component: str, tail: int = 100):
    thrust = []
    torque = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line or line.startswith("#"):
                continue
            try:
                fields = line.replace("(", " ").replace(")", " ").split()
                values = [float(value) for value in fields]
                if len(values) >= 7:
                    thrust.append(values[1])
                    torque.append(values[5])
            except (IndexError, ValueError):
                continue
    if not thrust:
        raise ValueError(f"No numeric force data found in {path}")
    result = thrust if component == "thrust" else torque
    return float(np.mean(np.array(result[-tail:])))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("forces_file", type=Path)
    parser.add_argument("--diameter", type=float, default=0.240)
    parser.add_argument("--rpm", type=float, default=600.0)
    parser.add_argument("--advance-speed", type=float, required=True)
    parser.add_argument("--rho", type=float, default=1000.0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    n = args.rpm / 60.0
    J = args.advance_speed / (n * args.diameter)
    thrust = mean_tail(args.forces_file, "thrust")
    torque = mean_tail(args.forces_file, "torque")
    KT = thrust / (args.rho * n**2 * args.diameter**4)
    KQ = torque / (args.rho * n**2 * args.diameter**5)
    eta = (J / (2 * np.pi)) * (KT / KQ) if KQ else float("nan")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["J", "KT", "10KQ", "eta0", "thrust_N", "torque_Nm"])
        writer.writerow([J, KT, 10*KQ, eta, thrust, torque])
    print(args.output)


if __name__ == "__main__":
    main()
