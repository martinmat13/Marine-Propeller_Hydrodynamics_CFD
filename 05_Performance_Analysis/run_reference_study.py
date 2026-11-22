#!/usr/bin/env python3
"""Generate the B5-75 reference curve and validate the coefficient reader."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
subprocess.run([sys.executable, str(ROOT / "02_Geometry" / "generate_reference_curve.py")], check=True)
