#!/usr/bin/bash

set -x

# =========================
# customize these as needed
# =========================

# where to save the installer script
LMTK_SETUP="${HOME}"/lmtk-setup.sh

# set to an absolute path (default is $HOME/lmod-toolkit)
LMTK_INSTALL_DIR="${HOME}"/lmod-toolkit

# dont actually do anything, just print out a list of commands
# that can be run manually
# MANUAL=yes

# set to "yes" or leave unset (defaults to latest)
# LMTK_ALLOW_PRE_RELEASE=yes

# set to "yes" to enable upgrading lmod-toolkit
# LMTK_ALLOW_UPGRADE=yes

# specify an exact version of LMTK
# get version string from
#    https://pypi.org/project/lmod-toolkit/#history      (production releases)
# OR https://test.pypi.org/project/lmod-toolkit/#history (pre-release versions)
# LMTK_INSTALL_VERSION=0.0.2.dev1794287670
# LMTK_INSTALL_VERSION=0.0.2

# either a branch name or leave unset (defaults to main)
# LMTK_GIT_BRANCH=poc

# specify a specific version of python if needed
# LMTK_UV_PYTHON=3.15

# =====================================
# shouldn't need to touch anything else
# =====================================


[[ -z "${LMTK_GIT_BRANCH}" ]] && LMTK_GIT_BRANCH=main
URL_BASE='https://raw.githubusercontent.com/access-ci-org/lmod-toolkit/refs/heads'
LMTK_SETUP_URL="${URL_BASE}"/"${LMTK_GIT_BRANCH}"/setup.sh
LMTK_UV_URL="${URL_BASE}"/"${LMTK_GIT_BRANCH}"/utils/uv_installer.sh
# LMTK_BIN="${LMTK_INSTALL_DIR}"/bin
VENV="${LMTK_INSTALL_DIR}"/.venv

###
# MAIN
###

# make exports (used by setup script)
export LMTK_UV_URL
export LMTK_INSTALL_DIR
[[ -n "${LMTK_ALLOW_PRE_RELEASE}" ]] && export LMTK_ALLOW_PRE_RELEASE
[[ -n "${LMTK_ALLOW_UPGRADE}" ]] && export LMTK_ALLOW_UPGRADE
[[ -n "${LMTK_UV_PYTHON}" ]] && export LMTK_UV_PYTHON
[[ -n "${LMTK_INSTALL_VERSION}" ]] && export LMTK_INSTALL_VERSION

# set ACTION if doing manual run
if [[ -n "${MANUAL}" ]] ; then
  ACTION=echo
  set +x
  echo 'COMMANDS THAT WOULD HAVE BEEN RUN'
  echo '---------------------------------'
fi

# stop anything running
# [[ -x "${IPF_BIN}"/wfm ]] && ${ACTION} bash "${IPF_BIN}"/wfm stop

# cleanup any existing installs
${ACTION} rm -rf "${LMTK_INSTALL_DIR}"
# ${ACTION} rm -rf "${HOME}"/.cache/pip #shouldn't need this anymore since switched to UV

# get new setup script
${ACTION} rm -f "${LMTK_SETUP}"
${ACTION} curl -o "${LMTK_SETUP}" "${LMTK_SETUP_URL}"
# and run it
${ACTION} bash "${LMTK_SETUP}"

# validate install
# ${ACTION} "${VENV}"/bin/python --version
# ${ACTION} "${VENV}"/bin/python -m pip freeze
