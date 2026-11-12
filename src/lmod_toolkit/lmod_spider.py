import functools
import json
import os
import pprint
import subprocess

from pathlib import Path

from lmod_toolkit import lmod_config


__all__ = [
    'as_json',
    'get_module_data',
    'get_module_files',
    'get_module_names',
]


@functools.cache
def get_module_data():
    prefix = lmod_config.prefix
    libexec = Path( prefix , 'lmod' , 'lmod' , 'libexec' )
    spider = libexec / 'spider'
    try:
        MODULEPATH = os.environ[ 'MODULEPATH' ] #will fail with KeyError if not found
    except KeyError as e:
        raise SystemExit( f"Missing environment variable 'MODULEPATH'\n{e}" )
    cmds = [ 'bash', '-l', '-c', f"{spider} -o jsonSoftwarePage \"{MODULEPATH}\"" ]
    result = subprocess.run(
        cmds,
        capture_output=True,  # Captures both stdout and stderr
        text=True             # Returns strings instead of bytes
    )
    return json.loads( result.stdout )


def get_module_names():
    return get_module_data().keys()


def get_module_files():
    return [
        v.keys()
        for v in get_module_data().values()
    ]


def as_json():
    return json.dumps( get_module_data() )


if __name__ == '__main__':
    pprint.pprint( get_module_data() )
