#!/usr/bin/bash

INSTALL_DIR=___INSTALL_DIR___
V_PYTHON="${INSTALLL_DIR}"/.venv/bin/python
SITE_PACKAGES=$(
  "${V_PYTHON}" -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])'
)
LMTK_PATH="${SITE_PACKAGES}"/lmod_toolkit

"${V_PYTHON}" "${LMTK_PATH}"/test.py
