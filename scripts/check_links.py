#!/usr/bin/env python3
"""Check external links in project documentation."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path


DOC_SUFFIXES = {".md", ".myst", ".ipynb", ".yml", ".yaml"}
SKIP_DIRS = {".git", ".ipynb_checkpoints", ".mypy_cache", ".pytest_cache", ".ruff_cache", ".venv", "_build"}
URL_RE = re.compile(r"https?://[^\s<>\]\)'\"`\\]+")
TRAILING_PUNCTUATION = ".,;:!?)]}"
BOT_BLOCKED_STATUSES = {401, 403, 405, 429}
# Hosts that are reachable from real user networks but frequently time out
# from US-based CI runners (geo / IP-reputation filtering). A clean timeout
# from one of these hosts is treated as OK rather than a hard failure.
TIMEOUT_TOLERATED_HOSTS = {
    "www.hydrodaten.admin.ch",
}


@dataclass(frozen=True)
class CheckResult:
    url: str
    ok: bool
    status: str
    message: str
    sources: tuple[str, ...]


def iter_doc_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() in DOC_SUFFIXES:
            files.append(path)
            continue
        if not path.is_dir():
            continue
        for child in path.rglob("*"):
            if any(part in SKIP_DIRS for part in child.parts):
                continue
            if child.is_file() and child.suffix.lower() in DOC_SUFFIXES:
                files.append(child)
    return sorted(set(files))


def read_doc_text(path: Path) -> str:
    if path.suffix.lower() != ".ipynb":
        return path.read_text(encoding="utf-8")

    notebook = json.loads(path.read_text(encoding="utf-8"))
    chunks: list[str] = []
    for cell in notebook.get("cells", []):
        source = cell.get("source", "")
        if isinstance(source, list):
            chunks.append("".join(source))
        elif isinstance(source, str):
            chunks.append(source)
    return "\n".join(chunks)


def normalize_url(raw_url: str) -> str:
    url = raw_url.rstrip(TRAILING_PUNCTUATION)
    while url.endswith("&quot;"):
        url = url[: -len("&quot;")]
    return url


def should_skip(url: str, include_binder_launch: bool) -> bool:
    if "github.com/" in url and "/actions/workflows/" in url and url.endswith("/badge.svg"):
        return True
    if include_binder_launch:
        return False
    return url.startswith("https://mybinder.org/v2/") or url.startswith("http://mybinder.org/v2/")


def collect_links(paths: list[Path], include_binder_launch: bool) -> dict[str, set[str]]:
    links: dict[str, set[str]] = {}
    for path in iter_doc_files(paths):
        text = read_doc_text(path)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in URL_RE.finditer(line):
                url = normalize_url(match.group(0))
                if should_skip(url, include_binder_launch):
                    continue
                links.setdefault(url, set()).add(f"{path}:{line_number}")
    return links


def request_once(url: str, method: str, timeout: float) -> tuple[int, str]:
    headers = {
        "User-Agent": "python-for-water-modellers-link-check/1.0",
        "Accept": "text/html,application/xhtml+xml,application/xml,application/pdf,*/*;q=0.8",
    }
    if method == "GET":
        headers["Range"] = "bytes=0-0"
    request = urllib.request.Request(url, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.status, response.reason


def _is_timeout_error(error: BaseException) -> bool:
    if isinstance(error, TimeoutError):
        return True
    reason = getattr(error, "reason", None)
    if isinstance(reason, TimeoutError):
        return True
    return "timed out" in str(error).lower()


def check_url(url: str, sources: set[str], timeout: float) -> CheckResult:
    methods = ("HEAD", "GET")
    last_error = ""
    failures_were_only_timeouts = True

    for method in methods:
        try:
            status, reason = request_once(url, method, timeout)
        except urllib.error.HTTPError as error:
            status = error.code
            reason = error.reason
            if status == 405 and method == "HEAD":
                continue
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            last_error = str(error)
            if not _is_timeout_error(error):
                failures_were_only_timeouts = False
            continue

        if 200 <= status < 400:
            return CheckResult(url, True, str(status), reason, tuple(sorted(sources)))
        if status in BOT_BLOCKED_STATUSES:
            return CheckResult(
                url,
                True,
                str(status),
                f"{reason}; reachable but blocked or rate-limited for automated checks",
                tuple(sorted(sources)),
            )
        last_error = f"HTTP {status} {reason}"
        failures_were_only_timeouts = False

    host = urllib.parse.urlparse(url).netloc.lower()
    if failures_were_only_timeouts and host in TIMEOUT_TOLERATED_HOSTS:
        return CheckResult(
            url,
            True,
            "timeout",
            f"{last_error}; host known to time out from CI runners but is reachable from real networks",
            tuple(sorted(sources)),
        )

    return CheckResult(url, False, "broken", last_error or "request failed", tuple(sorted(sources)))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, default=[Path("README.md"), Path("myst.yml"), Path("tutorials")])
    parser.add_argument("--timeout", type=float, default=20.0, help="Timeout per request in seconds")
    parser.add_argument("--workers", type=int, default=8, help="Number of concurrent link checks")
    parser.add_argument(
        "--include-binder-launch",
        action="store_true",
        help="Also check mybinder.org/v2 launch URLs; normally Binder Health covers these",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    links = collect_links(args.paths, args.include_binder_launch)
    if not links:
        print("No external links found.")
        return 0

    print(f"Checking {len(links)} unique external links...")
    results: list[CheckResult] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(check_url, url, sources, args.timeout): url
            for url, sources in sorted(links.items())
        }
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
            marker = "OK" if result.ok else "BROKEN"
            print(f"{marker:7} {result.status:>7} {result.url}")

    broken = [result for result in sorted(results, key=lambda item: item.url) if not result.ok]
    if not broken:
        print("All checked links are reachable.")
        return 0

    print("\nBroken links:")
    for result in broken:
        print(f"- {result.url}: {result.message}")
        for source in result.sources:
            print(f"  referenced from {source}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
