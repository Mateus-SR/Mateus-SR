#!/usr/bin/env python3
"""Recolor arcade contribution graph SVGs with the 8-Bit Ocean palette."""
from pathlib import Path
import sys
LIGHT = {
    "#57606a": "#09474a", "#ebedf0": "#b7e1cd", "#40c463": "#007D7A",
    "#9be9a8": "#3dbf8c", "#30a14e": "#09474a", "#216e39": "#caff23",
}
DARK = {
    "#0d1117": "#09474a", "#8b949e": "#b7e1cd", "#161b22": "#09474a",
    "#0e4429": "#007D7A", "#006d32": "#3dbf8c", "#26a641": "#b7e1cd",
    "#39d353": "#caff23",
}
def main():
    if len(sys.argv) < 2:
        raise SystemExit("Pass one or more SVG paths.")
    for raw in sys.argv[1:]:
        path = Path(raw)
        if not path.is_file():
            raise FileNotFoundError(path)
        mapping = DARK if path.name.endswith("-dark.svg") else LIGHT
        svg = path.read_text(encoding="utf-8")
        for source, target in mapping.items():
            svg = svg.replace(source, target)
        path.write_text(svg, encoding="utf-8")
        print(f"Applied palette: {path}")
if __name__ == "__main__":
    main()
