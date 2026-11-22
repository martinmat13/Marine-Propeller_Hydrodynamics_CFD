#!/usr/bin/env bash
set -euo pipefail

source /usr/lib/openfoam/openfoam2512/etc/bashrc

python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install numpy pandas matplotlib scipy

echo "OpenFOAM v2512 and Python environment initialized."
