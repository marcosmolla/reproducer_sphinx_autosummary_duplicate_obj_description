#!/bin/bash
set -e

# Setup (requires-python >= 3.13 in pyproject.toml ensures correct version)
uv sync

# Generate .rst files via sphinx-apidoc
rm -rf docs/generated docs/_build
uv run sphinx-apidoc \
    -o docs/generated \
    --implicit-namespaces \
    --module-first --separate --remove-old \
    src/mypackage

# Build docs with warnings as errors
SPHINX_APIDOC_OPTIONS=members,show-inheritance \
  uv run sphinx-build -W --keep-going --builder html docs docs/_build
