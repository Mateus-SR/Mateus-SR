#!/usr/bin/env python3
"""Apply the 8-Bit Ocean palette to the six profile-cards-action SVGs.

The generator remains on its documented blue source palette. Repository
language brand colors are deliberately left untouched.
"""
from pathlib import Path

DARK_MAP = {
    "#0d1117": "#09474a", "#151b23": "#007D7A", "#3d444d": "#3dbf8c",
    "#262c34": "#3dbf8c", "#21262d": "#09474a", "#1f2328": "#09474a",
    "#f0f6fc": "#FFFFFF", "#9198a1": "#FFFFFF", "#4493f8": "#caff23",
    "#161b22": "#09474a", "#22385f": "#007D7A", "#024386": "#007D7A",
    "#205a9f": "#3dbf8c", "#0876ca": "#3dbf8c", "#0f8ef1": "#b7e1cd",
    "#579ee4": "#b7e1cd", "#70b7ff": "#caff23", "#3fb950": "#3dbf8c",
    "#a371f7": "#007D7A", "#db6d28": "#caff23", "#6e7681": "#b7e1cd",
}
LIGHT_MAP = {
    "#f6f8fa": "#b7e1cd", "#d1d9e0": "#007D7A", "#e4e8ec": "#b7e1cd",
    "#eaeef2": "#b7e1cd", "#1f2328": "#09474a", "#59636e": "#007D7A",
    "#0969da": "#007D7A", "#ebedf0": "#b7e1cd", "#b7d6ff": "#3dbf8c",
    "#90c0fe": "#3dbf8c", "#66a9fe": "#007D7A", "#539ffc": "#3dbf8c",
    "#4372b1": "#09474a", "#3d89e4": "#caff23", "#2f5d9b": "#09474a",
    "#1a7f37": "#3dbf8c", "#8250df": "#007D7A", "#bc4c00": "#caff23",
    "#8b949e": "#007D7A",
}
FILES = {
    "overview.dark.svg": DARK_MAP, "lifetime.dark.svg": DARK_MAP,
    "repositories.dark.svg": DARK_MAP, "overview.light.svg": LIGHT_MAP,
    "lifetime.light.svg": LIGHT_MAP, "repositories.light.svg": LIGHT_MAP,
}

def main():
    for name, palette in FILES.items():
        path = Path("assets") / name
        if not path.is_file():
            raise FileNotFoundError(path)
        svg = path.read_text(encoding="utf-8")
        for source, target in palette.items():
            svg = svg.replace(source, target)
        path.write_text(svg, encoding="utf-8")
        print(f"Applied palette: {path}")

if __name__ == "__main__":
    main()
