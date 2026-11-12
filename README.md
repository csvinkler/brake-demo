# brake-demo

![CI](../../actions/workflows/ci.yml/badge.svg)

A tiny ABS (anti-lock braking) function used to show test automation and CI/CD with GitHub Actions.
Not real ECU code.

## Try it in 5 minutes, only with a browser

1. Click **Use this template > Create a new repository** (public). You now own a copy.
2. Open the **Actions** tab. The **CI** workflow already runs for your first commit.
3. Break something: open `src/brake_demo/abs.py`, press the pencil icon, change
   `SLIP_THRESHOLD = 0.20` to `0.30` and commit. Watch CI turn red and find the failing test.
4. Change it back and commit. CI is green again.
5. Release: **Actions > Release > Run workflow**, version `v1.0.0`. After about a minute a new
   release with the built package appears under **Releases**.

## What runs when

| Event | Workflow | Steps |
|---|---|---|
| push to `main`, pull request | `ci.yml` | ruff lint, then pytest on Python 3.10 / 3.12 / 3.13, coverage at least 90 %, test report as artifact |
| tag `v*` or manual run | `release.yml` | runs CI first, checks tag = version in code, builds wheel, smoke test, publishes a GitHub release |

## Run locally (optional)

```bash
pip install -e ".[test]"
ruff check .
pytest -v
brake-demo 100 70      # slip = 30%  ->  ABS RELEASE
```

## Requirements and tests

Each requirement in `src/brake_demo/abs.py` (REQ-ABS-01 to 05) has a test with the same ID in
`tests/test_abs.py`, so a red test points straight to the broken requirement.
