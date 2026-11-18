#!/usr/bin/bash

INSTALL_DIR=___INSTALL_DIR___

set -x

CMD=$( basename $0 '.sh' )

OPT="--$CMD"

PYTHON="${INSTALL_DIR}"/.venv/bin/python

$PYTHON -m lmod_toolkit "$OPT"
