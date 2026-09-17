#!/usr/bin/env python3
"""Compatibility entry point for the canonical XV2 skill-data build.

The repository previously had two independent skill generators. Keeping a second
scraper here allowed scheduled/manual runs to overwrite the canonical research model.
The authoritative implementation now lives in build_skills_from_research.py.
"""
from __future__ import annotations
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build_skills_from_research.py"

if __name__ == "__main__":
    runpy.run_path(str(BUILDER), run_name="__main__")
