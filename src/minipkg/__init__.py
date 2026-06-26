"""minipkg package.

Minimal packaging example with uv and pyproject.toml
"""

from __future__ import annotations

from minipkg._internal.cli import get_parser, main

__all__: list[str] = ["get_parser", "main"]
