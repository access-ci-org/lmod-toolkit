import functools
import json
import os
import pprint
import subprocess

from pathlib import Path

import lmod_toolkit as lmtk


__all__ = [
    'as_json',
    'get_modulepath',
    'get_module_data',
    'get_module_files',
    'get_module_names',
]


def get_modulepath():
    current_resource = lmtk.config.get_current_resource_definition()
    current_modulepath = current_resource.get( 'modulepath', None )
    # If current modulepath is None, try to get it from the environment
    if current_modulepath is None:
        try:
            current_modulepath = os.environ[ 'MODULEPATH' ]
        except KeyError as e:
            raise SystemExit( f"Missing environment variable 'MODULEPATH'\n{e}" )
    return current_modulepath


def get_module_data():
    ''' Wrapper around get_lmod_spider_software_page
        passing the current value of MODULEPATH
        so that functools.cache works as expected,
        caching the results for a given modulepath
    '''
    current_modulepath = get_modulepath()
    return get_lmod_spider_software_page( modulepath=current_modulepath )


def get_module_names():
    return get_module_data().keys()


def get_module_files():
    return [
        v.keys()
        for v in get_module_data().values()
    ]


def as_dict():
    return get_module_data()


def as_json():
    return json.dumps( as_dict() )


@functools.cache
def get_lmod_spider_software_page( modulepath ):
    spider = lmtk.lmod_config.get_spider_path()
    cmds = [ 'bash', '-l', '-c', f"{spider} -o jsonSoftwarePage \"{modulepath}\"" ]
    result = subprocess.run(
        cmds,
        capture_output=True,  # Captures both stdout and stderr
        text=True             # Returns strings instead of bytes
    )
    return json.loads( result.stdout )


if __name__ == '__main__':
    pprint.pprint( get_module_data() )
