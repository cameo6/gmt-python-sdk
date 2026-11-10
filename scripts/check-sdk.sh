#!/bin/sh
set -eu

cd "$(dirname "$0")/.."
repo=$(pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

sh scripts/sdk/generate.sh python "$work"
python3 -m venv "$work/build-env"
"$work/build-env/bin/python" -m pip install build==1.2.2.post1
"$work/build-env/bin/python" -m build --outdir "$work/packages" "$work/python"

for archive in "$work/packages/"*.whl "$work/packages/"*.tar.gz; do
  install_env="$work/install-${archive##*/}"
  python3 -m venv "$install_env"
  python="$install_env/bin/python"
  "$python" -m pip install "$archive"
  "$python" -B "$repo/scripts/compat/check-examples.py" "$work/openapi.json" python
  PYTHONDONTWRITEBYTECODE=1 SDK_COMPAT_RELEASE=1 "$python" "$repo/scripts/compat/run.py" python
done

mkdir -p dist
(
  cd "$work/packages"
  shasum -a 256 ./*.whl ./*.tar.gz > SHA256SUMS
  cp ./*.whl ./*.tar.gz SHA256SUMS "$repo/dist/"
)
