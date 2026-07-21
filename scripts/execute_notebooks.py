#!/usr/bin/env python3
"""Execute tutorial notebooks and report any cell that raises.

Nothing else in CI runs the notebooks: `myst build --html` renders the outputs
already stored in each file, so a dependency upgrade can break every tutorial
while the site still builds and every other check passes. This script executes
them for real against the installed environment.

Notebooks are executed in memory and never written back, so stored outputs stay
as committed and the run produces no notebook diff.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*m")


@dataclass(frozen=True)
class ExecutionResult:
    notebook: Path
    ok: bool
    message: str


def iter_notebooks(paths: list[Path]) -> list[Path]:
    notebooks: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix == ".ipynb":
            notebooks.append(path)
            continue
        if not path.is_dir():
            continue
        notebooks.extend(
            child
            for child in path.rglob("*.ipynb")
            if ".ipynb_checkpoints" not in child.parts
        )
    return sorted(set(notebooks))


def summarise_failure(error: CellExecutionError) -> str:
    """Return the last few lines of a traceback, which name the actual error.

    IPython colours tracebacks with ANSI escapes that are unreadable in a CI
    log, so strip them.
    """
    plain = ANSI_ESCAPE_RE.sub("", str(error))
    lines = [line.rstrip() for line in plain.strip().splitlines() if line.strip()]
    return "\n".join(lines[-8:])


def execute_notebook(notebook: Path, timeout: float, kernel: str) -> ExecutionResult:
    document = nbformat.read(notebook, as_version=4)
    client = NotebookClient(
        document,
        timeout=timeout,
        kernel_name=kernel,
        # Relative paths in a notebook resolve against its own directory, the
        # same way they do for a reader running it in Jupyter.
        resources={"metadata": {"path": str(notebook.parent)}},
        allow_errors=False,
    )
    try:
        client.execute()
    except CellExecutionError as error:
        return ExecutionResult(notebook, False, summarise_failure(error))
    except Exception as error:  # noqa: BLE001 - report, do not mask, any failure
        return ExecutionResult(notebook, False, f"{type(error).__name__}: {error}")
    return ExecutionResult(notebook, True, "")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, default=[Path("tutorials")])
    parser.add_argument("--timeout", type=float, default=300.0, help="Timeout per cell in seconds")
    parser.add_argument("--kernel", default="python3", help="Kernel name to execute with")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    notebooks = iter_notebooks(args.paths)
    if not notebooks:
        # Treat "nothing to execute" as a failure: in CI it almost always means
        # a renamed directory or a mistyped path, which would otherwise pass
        # silently having executed nothing.
        print("No notebooks found.", file=sys.stderr)
        return 1

    print(f"Executing {len(notebooks)} notebooks...")
    results: list[ExecutionResult] = []
    for notebook in notebooks:
        result = execute_notebook(notebook, args.timeout, args.kernel)
        results.append(result)
        print(f"{'OK' if result.ok else 'FAILED':7} {notebook}", flush=True)

    failures = [result for result in results if not result.ok]
    if not failures:
        print(f"\nAll {len(results)} notebooks executed cleanly.")
        return 0

    print(f"\n{len(failures)} of {len(results)} notebooks failed:")
    for result in failures:
        print(f"\n- {result.notebook}")
        for line in result.message.splitlines():
            print(f"    {line}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
