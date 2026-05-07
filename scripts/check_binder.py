#!/usr/bin/env python3
"""Launch Binder and verify that the resulting Jupyter server responds."""

from __future__ import annotations

import argparse
import json
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


USER_AGENT = "python-for-water-modellers-binder-health/1.0"


class BinderCheckError(RuntimeError):
    """Raised when Binder does not become usable."""


def request(url: str, *, method: str = "GET", timeout: float = 30.0):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": USER_AGENT}, method=method),
        timeout=timeout,
    )


def build_url(binder_url: str, repo: str, ref: str, urlpath: str | None) -> str:
    base = binder_url.rstrip("/")
    encoded_ref = urllib.parse.quote(ref, safe="")
    url = f"{base}/build/gh/{repo}/{encoded_ref}"
    if urlpath:
        url = f"{url}?{urllib.parse.urlencode({'urlpath': urlpath})}"
    return url


def wait_for_ready(build_endpoint: str, timeout: float) -> tuple[str, str]:
    deadline = time.monotonic() + timeout
    request_obj = urllib.request.Request(
        build_endpoint,
        headers={"Accept": "text/event-stream", "User-Agent": USER_AGENT},
    )

    try:
        response = urllib.request.urlopen(request_obj, timeout=30)
    except urllib.error.URLError as error:
        raise BinderCheckError(f"Could not open Binder build stream: {error}") from error

    with response:
        while time.monotonic() < deadline:
            try:
                line = response.readline()
            except (TimeoutError, socket.timeout) as error:
                raise BinderCheckError(f"Timed out while waiting for Binder build events: {error}") from error

            if not line:
                raise BinderCheckError("Binder build stream closed before reporting ready")

            decoded = line.decode("utf-8", errors="replace").strip()
            if not decoded.startswith("data:"):
                continue

            payload = decoded.removeprefix("data:").strip()
            if not payload:
                continue

            try:
                event = json.loads(payload)
            except json.JSONDecodeError:
                print(f"binder event: {payload}")
                continue

            phase = event.get("phase", "unknown")
            message = event.get("message", "")
            print(f"binder phase: {phase} {message}".rstrip())

            if phase == "failed":
                raise BinderCheckError(message or "Binder build failed")
            if phase == "ready":
                server_url = event.get("url")
                token = event.get("token", "")
                if not server_url:
                    raise BinderCheckError("Binder reported ready without a server URL")
                return server_url, token

    raise BinderCheckError(f"Binder was not ready after {timeout:.0f} seconds")


def with_token(url: str, token: str) -> str:
    if not token:
        return url
    separator = "&" if urllib.parse.urlsplit(url).query else "?"
    return f"{url}{separator}{urllib.parse.urlencode({'token': token})}"


def check_jupyter_server(server_url: str, token: str, urlpath: str | None) -> None:
    root = server_url.rstrip("/") + "/"
    status_url = with_token(urllib.parse.urljoin(root, "api/status"), token)
    with request(status_url, timeout=30) as response:
        if response.status != 200:
            raise BinderCheckError(f"Jupyter status endpoint returned HTTP {response.status}")
        payload = json.loads(response.read().decode("utf-8"))
        print(f"jupyter status: kernels={payload.get('kernels')} connections={payload.get('connections')}")

    if urlpath:
        launch_url = with_token(urllib.parse.urljoin(root, urlpath), token)
        with request(launch_url, timeout=30) as response:
            if response.status >= 400:
                raise BinderCheckError(f"Jupyter launch path returned HTTP {response.status}")
            print(f"launch path OK: {urlpath}")


def shutdown_jupyter_server(server_url: str, token: str) -> None:
    if not server_url:
        return
    root = server_url.rstrip("/") + "/"
    shutdown_url = with_token(urllib.parse.urljoin(root, "api/shutdown"), token)
    try:
        with request(shutdown_url, method="POST", timeout=15) as response:
            print(f"shutdown requested: HTTP {response.status}")
    except Exception as error:  # noqa: BLE001 - best-effort cleanup only
        print(f"shutdown warning: {error}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binder-url", default="https://mybinder.org")
    parser.add_argument("--repo", default="mabesa/python-for-water-modellers")
    parser.add_argument("--ref", default="main")
    parser.add_argument("--timeout", type=float, default=900.0)
    parser.add_argument("--urlpath", default="lab/tree/tutorials/00_introduction.ipynb")
    parser.add_argument("--skip-shutdown", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    endpoint = build_url(args.binder_url, args.repo, args.ref, args.urlpath)
    print(f"launching Binder: {endpoint}")
    server_url = ""
    token = ""

    try:
        server_url, token = wait_for_ready(endpoint, args.timeout)
        print(f"binder ready: {server_url}")
        check_jupyter_server(server_url, token, args.urlpath)
    except BinderCheckError as error:
        print(f"Binder health check failed: {error}", file=sys.stderr)
        return 1
    finally:
        if server_url and not args.skip_shutdown:
            shutdown_jupyter_server(server_url, token)

    print("Binder health check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
