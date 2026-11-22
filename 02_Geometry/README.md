# Propeller geometry and reference data

## Selected baseline configuration

| Item | Value |
|---|---|
| Series | Wageningen B-series |
| Designation | B5-75 |
| Blades | 5 |
| Diameter | 0.240 m |
| Pitch ratio P/D | 1.20 |
| Expanded area ratio AE/A0 | 0.75 |
| Hub diameter ratio | 1/6 |
| Geometry status | Parametric reconstruction |

The repository uses a published B-series configuration and public regression
laws. The generated surface is a reconstruction from documented dimensional
laws, not original NSMB or MARIN coordinate records.

## Use restriction

Do not describe the generated STL as measured or exact geometry. It is suitable
for a transparent code-development baseline and mesh-workflow demonstration.
Physical validation requires original model-test coordinates and raw open-water
measurements for the same configuration.

## Required configuration record

Before CFD begins, the repository must record:

| Parameter | Status |
|---|---|
| Blade count | Selected: 5 |
| Diameter | Selected: 0.240 m |
| Pitch ratio | Selected: 1.20 |
| Expanded area ratio | Selected: 0.75 |
| Hub dimensions | Selected: d/D = 1/6 |
| Radial section coordinates | Reconstructed from published dimensional laws |
| Section profiles | Parametric approximation |
| Skew and rake | Skew/rake omitted |
| Experimental reference curve | No raw curve included; polynomial reference only |
| License or redistribution terms | Polynomial source documented; no copied raw geometry |

## Selection rule

A valid configuration must satisfy all of these conditions:

1. The geometry and performance data name the same B-series configuration.
2. Coordinate data or a documented reconstruction method are accessible.
3. A source provides the blade count, pitch ratio, expanded area ratio, and
   enough radial dimensions to reproduce or prepare a defensible model.
4. The reference permits the intended public repository use.
5. All assumptions are disclosed if an exact geometry or experimental dataset
   cannot be included.

## Defensible outcomes

There are three acceptable outcomes:

1. Include fully licensed geometry and reference data.
2. Include a documented script that fetches geometry from an explicitly
   identified source permitted for the selected use.
3. State that an authentic comparison is unavailable and limit the repository
   to a B-series performance-model study or independently owned geometry.

The repository must never present a hand-built stylized blade as an authentic
Wageningen B-series propeller.
