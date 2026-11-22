#!/usr/bin/env bash
set -euo pipefail

echo "OpenFOAM environment"
echo "WM_PROJECT_VERSION=${WM_PROJECT_VERSION:-not-set}"
echo "FOAM_APPBIN=${FOAM_APPBIN:-not-set}"

for command_name in \
    blockMesh snappyHexMesh checkMesh simpleFoam decomposePar reconstructPar
do
    if command -v "$command_name" >/dev/null 2>&1; then
        printf "FOUND  %s: %s\n" "$command_name" "$(command -v "$command_name")"
    else
        printf "MISSING %s\n" "$command_name"
    fi
done

echo
echo "Python"
python3 --version

for module_name in numpy pandas matplotlib scipy; do
    python3 -c "import $module_name; print('$module_name', getattr($module_name, '__version__', 'installed'))"
done

echo
echo "Geometry tools"
for command_name in gmsh freecad FreeCADCmd blender openscad; do
    if command -v "$command_name" >/dev/null 2>&1; then
        printf "FOUND  %s: %s\n" "$command_name" "$(command -v "$command_name")"
    else
        printf "MISSING %s\n" "$command_name"
    fi
done

echo
echo "Resources"
printf "Logical CPU cores: "
nproc
free -h
