"""Minimal Sphinx config to reproduce duplicate object warnings with generic pydantic models."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

project = "pep695-sphinx-repro"
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
]
