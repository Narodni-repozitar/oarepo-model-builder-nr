#!/bin/bash

set -e

rm -rf .venv-builder

python3 -m venv .venv-builder

.venv-builder/bin/pip install -U setuptools pip wheel
.venv-builder/bin/pip install -e .

(
    cd tests
    rm -rf nr-common-test-model
    ../.venv-builder/bin/oarepo-compile-model nr_common_metadata_model.yaml -vvv --output-directory nr-common-test-model
)
(
    cd tests
    rm -rf nr-theses-test-model
    ../.venv-builder/bin/oarepo-compile-model nr_theses_metadata_model.yaml -vvv --output-directory nr-theses-test-model
)