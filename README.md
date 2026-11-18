# lmod toolkit
Tools for working with lmod

## Install
* `curl -o lmtk-setup.sh
https://raw.githubusercontent.com/access-ci-org/lmod-toolkit/refs/heads/main/setup.sh
`
* `./lmtk-setup.sh`
* `~/lmod-toolkit/bin/mkcfg.sh`
* Edit config file (from previous step)
* `~/lmod-toolkit/bin/test.sh`
* `~/lmod-toolkit/bin/publish.sh`

# Design
Config holds a list of Resource Definitions to be reported on.

Publish loops over each Resource Definition and for each,
* gathers & publishes:
  * lmod_spider (available software modules)
  * lmod_extended_attributes

It does this via Config.iter_resources(), a Python generator function.

Each iteration of iter_resources moves to a new Resource Definition and saves
the current Resource Definition.

lmod_spider and lmod_ext_attrs will ask Config for
"current_resource_definition" and do their work relative to any settings given
therein.
