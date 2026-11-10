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
