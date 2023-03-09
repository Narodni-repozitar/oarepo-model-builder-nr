#!/bin/bash

set -e

if [ -d .venv-builder ] ; then
    rm -rf .venv-builder
fi

python3 -m venv .venv-builder

.venv-builder/bin/pip install -U setuptools pip wheel
.venv-builder/bin/pip install -e .

(
    cd tests
    rm -rf nr-common-test-model
    ../.venv-builder/bin/oarepo-compile-model nr_common_metadata_model.yaml -vvv --output-directory nr-common-test-model
)