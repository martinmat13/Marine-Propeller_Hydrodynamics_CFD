#!/usr/bin/env bash
set -euo pipefail

for J in 0.2 0.4 0.6 0.8 1.0 1.2; do
    VA=$(python3 -c "print(f'{float(\"$J\")*10*0.240:.6f}')")
    echo "Prepared condition J=${J}, n=10 rps, VA=${VA} m/s"
done
