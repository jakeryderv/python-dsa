#!/usr/bin/env python
"""Guard against stale saved outputs.

`nbmake` proves every notebook *executes*, but it runs in memory and never
checks that the outputs committed to disk actually match the current code — so
a notebook whose code changed but wasn't re-run can pass CI with stale outputs.

This script re-executes each notebook and diffs the committed code-cell outputs
against the fresh run, with volatile tokens normalised away:

  * numbers      -> N      (timeit / getsizeof / measured rates jitter run-to-run)
  * 0x<hex>      -> 0xADDR (object reprs)

so a forgotten re-run (changed code, structurally different output, a new/removed
cell, or an error) is caught, while benign timing noise is not.

Usage:  uv run python scripts/check_outputs_fresh.py [notebook ...]
        (no args -> every notebook under the four numbered tiers)
"""
from __future__ import annotations

import copy
import pathlib
import re
import sys

import nbformat
from nbclient import NotebookClient

TIERS = ["0-foundations", "1-data-structures", "2-algorithms", "3-patterns"]

_HEX = re.compile(r"0x[0-9a-fA-F]+")
_NUM = re.compile(r"[-+]?\d[\d_]*\.?\d*(?:[eE][-+]?\d+)?")
_WS = re.compile(r"\s+")


def normalise(text: str) -> str:
    text = _HEX.sub("0xADDR", text)
    text = _NUM.sub("N", text)
    # Collapse internal whitespace too: right-justified numeric columns shift
    # their padding when a measured value changes width (e.g. 9.87 -> 10.11),
    # and that spacing would otherwise survive number-normalisation.
    return "\n".join(_WS.sub(" ", line).strip() for line in text.strip().splitlines())


def cell_outputs(cell) -> str:
    parts: list[str] = []
    for o in cell.get("outputs", []):
        t = o.get("output_type")
        if t == "stream":
            parts.append(o.get("text", ""))
        elif t in ("execute_result", "display_data"):
            parts.append(o.get("data", {}).get("text/plain", ""))
        elif t == "error":
            parts.append("\n".join(o.get("traceback", [])))
    return normalise("".join(parts))


def check(path: pathlib.Path) -> list[object]:
    nb = nbformat.read(str(path), as_version=4)
    committed = [cell_outputs(c) for c in nb.cells if c.cell_type == "code"]

    fresh_nb = copy.deepcopy(nb)
    NotebookClient(fresh_nb, timeout=180, kernel_name="python3").execute()
    fresh = [cell_outputs(c) for c in fresh_nb.cells if c.cell_type == "code"]

    drift: list[object] = []
    if len(committed) != len(fresh):
        return ["cell-count changed"]
    for i, (a, b) in enumerate(zip(committed, fresh)):
        if a != b:
            drift.append(i)
    return drift


def main(argv: list[str]) -> int:
    if argv:
        notebooks = [pathlib.Path(a) for a in argv]
    else:
        root = pathlib.Path(__file__).resolve().parent.parent
        notebooks = sorted(p for tier in TIERS for p in (root / tier).glob("*.ipynb"))

    stale: dict[str, list[object]] = {}
    for p in notebooks:
        drift = check(p)
        print(f"{'STALE' if drift else 'ok':5}  {p}")
        if drift:
            stale[str(p)] = drift

    if stale:
        print("\nStale notebooks — saved outputs differ from a fresh run "
              "(after normalising numbers/addresses):")
        for name, cells in stale.items():
            print(f"  {name}: code cells {cells}")
        print("\nRe-run them:  uv run jupyter nbconvert --to notebook "
              "--execute --inplace <notebook>")
        return 1

    print(f"\nAll {len(notebooks)} notebooks fresh.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
