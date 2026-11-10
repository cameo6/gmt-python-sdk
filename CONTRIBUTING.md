# Contributing to the GMT Python SDK

Use Python 3.11 or later and Docker to run the repository checks. The SDK
itself supports Python 3.9 or later.

```sh
sh scripts/check-sdk.sh
```

The check regenerates the internal routes and code-page model from the
committed `openapi.json`, then compares them with the checked-in files. It
builds a wheel and a source distribution in a temporary directory. Each
distribution is installed in a fresh virtual environment and checked against
the OpenAPI examples and the synchronous and asynchronous compatibility
tests. The verified distributions and `SHA256SUMS` are copied to `dist/`.
GitHub Actions also uploads them as build artifacts.

When changing `openapi.json`, update the generated files from the repository
root and review the resulting source diff:

```sh
workdir=$(mktemp -d)
sh scripts/sdk/generate.sh python "$workdir" --update
rm -rf "$workdir"
```

The generated files are checked in so the SDK can also be installed directly
from a checkout without running the generator:

```sh
python -m pip install .
```

The public resource methods and response models live under `src/gmt`.
Review them when the contract changes and keep the compatibility checks
aligned with the public API. See the [GMT API reference](https://api.getmytg.com/docs)
for the current endpoints and examples.

## Release workflow

The release workflow builds and tests installable packages and uploads
`pypi-release-candidate` with `SHA256SUMS`. Pull requests that change the release
workflow run these checks automatically. After merge, run the workflow on
`main` with `publish` left off to verify a candidate without registry writes.

Before the first release, configure the GitHub `pypi` environment to allow
only `main` and require a release reviewer. In the registry settings for
`gmt-python-sdk`, add a GitHub Actions Trusted Publisher
using these values:

| Setting | Value |
| --- | --- |
| Owner | `cameo6` |
| Repository | `gmt-python-sdk` |
| Workflow filename | `release.yml` |
| GitHub environment | `pypi` |

For a release, select `main`, enable `publish`, and enter the new stable version
from `pyproject.toml`. The publish job downloads the tested artifact from the same
run, checks SHA-256, and authenticates via OIDC.

[Trusted Publishing setup](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)
