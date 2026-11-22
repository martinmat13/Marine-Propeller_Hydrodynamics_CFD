#!/usr/bin/env python3
"""Generate a parametric five-bladed Wageningen B-series reconstruction."""

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config.json").read_text())

D = float(CONFIG["diameter_m"])
R = D / 2.0
Z = int(CONFIG["blades"])
EAR = float(CONFIG["expanded_area_ratio"])
P_D = float(CONFIG["pitch_ratio"])

RADIAL_R = np.array([0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.975])
CONTOUR_K = np.array([1.662, 1.882, 2.050, 2.152, 2.187, 2.144, 1.970, 1.582, 1.434, 1.122])
AR = np.array([0.0526, 0.0464, 0.0402, 0.0340, 0.0278, 0.0216, 0.0154, 0.0092, 0.0092, 0.0092])
BR = np.array([0.0040, 0.0035, 0.0030, 0.0025, 0.0020, 0.0015, 0.0010, 0.0005, 0.0005, 0.0005])
PITCH_FACTOR = np.array([0.882, 0.887, 0.950, 0.992, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])


def write_ascii_stl(path: Path, triangles):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="ascii") as handle:
        handle.write("solid propeller_reconstruction\n")
        for a, b, c in triangles:
            ab = b - a
            ac = c - a
            normal = np.cross(ab, ac)
            norm = np.linalg.norm(normal)
            normal = normal / norm if norm else np.zeros(3)
            handle.write("  facet normal {:.9e} {:.9e} {:.9e}\n".format(*normal))
            handle.write("    outer loop\n")
            for vertex in (a, b, c):
                handle.write("      vertex {:.9e} {:.9e} {:.9e}\n".format(*vertex))
            handle.write("    endloop\n")
            handle.write("  endfacet\n")
        handle.write("endsolid propeller_reconstruction\n")


def add_quad(triangles, a, b, c, d):
    triangles.append((a, b, c))
    triangles.append((a, c, d))


def add_cylinder(triangles, radius, x_min, x_max, segments=32):
    centre_x_min = np.array([x_min, 0.0, 0.0])
    centre_x_max = np.array([x_max, 0.0, 0.0])
    for i in range(segments):
        theta0 = 2.0 * math.pi * i / segments
        theta1 = 2.0 * math.pi * (i + 1) / segments
        p0 = np.array([x_min, radius * math.cos(theta0), radius * math.sin(theta0)])
        p1 = np.array([x_min, radius * math.cos(theta1), radius * math.sin(theta1)])
        q0 = np.array([x_max, radius * math.cos(theta0), radius * math.sin(theta0)])
        q1 = np.array([x_max, radius * math.cos(theta1), radius * math.sin(theta1)])
        add_quad(triangles, p0, q0, q1, p1)
        triangles.append((centre_x_min, p1, p0))
        triangles.append((centre_x_max, q0, q1))


def section_points(r_over_r, phase):
    r = r_over_r * R
    k = float(np.interp(r_over_r, RADIAL_R, CONTOUR_K, left=CONTOUR_K[0], right=0.0))
    ar = float(np.interp(r_over_r, RADIAL_R, AR))
    br = float(np.interp(r_over_r, RADIAL_R, BR))
    pitch_factor = float(np.interp(r_over_r, RADIAL_R, PITCH_FACTOR))
    chord = k * EAR * D / Z
    thickness = D * (ar - br * Z)
    beta = math.atan(P_D * pitch_factor / (2.0 * math.pi * r_over_r))

    tangential = np.array([0.0, -math.sin(phase), math.cos(phase)])
    radial = np.array([0.0, math.cos(phase), math.sin(phase)])
    axial_center = r * 0.02 * math.sin(2.0 * math.pi * r_over_r)
    points = []
    for u in (-0.5, -0.25, 0.0, 0.25, 0.5):
        chord_offset = u * chord
        thickness_factor = 1.0 - 4.0 * u * u
        axial = axial_center + chord_offset * math.sin(beta) + thickness * thickness_factor * 0.45 * math.cos(beta)
        point = radial * r + tangential * chord_offset * math.cos(beta)
        point[0] = axial
        points.append(point)
    return points


def main():
    triangles = []
    add_cylinder(triangles, R * float(CONFIG["hub_diameter_ratio"]), -0.12, 0.12)
    radial_stations = np.linspace(0.20, 1.0, 17)
    for blade in range(Z):
        phase = 2.0 * math.pi * blade / Z
        rings = [section_points(float(x), phase) for x in radial_stations]
        for i in range(len(rings) - 1):
            for j in range(len(rings[i]) - 1):
                add_quad(triangles, rings[i][j], rings[i + 1][j], rings[i + 1][j + 1], rings[i][j + 1])
        inner = rings[0]
        for j in range(len(inner) - 1):
            edge = np.array([0.0, -0.001, 0.0])
            add_quad(triangles, inner[j], inner[j + 1], inner[j + 1] + edge, inner[j] + edge)

    output = ROOT / "outputs" / "propeller_b5_75_reconstruction.stl"
    write_ascii_stl(output, triangles)
    print(f"Generated {output}")
    print(f"D={D:.3f} m, Z={Z}, P/D={P_D:.3f}, EAR={EAR:.3f}")


if __name__ == "__main__":
    main()
