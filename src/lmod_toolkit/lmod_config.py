import functools
import json
import pprint
import subprocess
import sys

from pathlib import Path

__all__ = [
    'as_json',
    'get_config',
    'get_spider_path',
]

@functools.cache
def get_config():
    cmds = [ 'bash', '-l', '-c', 'module --config_json' ]
    result = subprocess.run(
        cmds,
        capture_output=True,  # Captures both stdout and stderr
        text=True             # Returns strings instead of bytes
    )
    return json.loads( result.stderr )


@functools.cache
def get_spider_path():
    this_py_module = sys.modules[ __name__ ]
    prefix = this_py_module.prefix
    libexec = Path( prefix , 'lmod' , 'lmod' , 'libexec' )
    return libexec / 'spider'


def as_dict():
    return get_config()


def as_json():
    return json.dumps( as_dict() )


def __getattr__( name ):
    cfg = get_config()
    try:
        val = cfg['configT'][name]
    except KeyError as e:
        raise AttributeError( f"'{name}' not found" )
    return val


if __name__ == '__main__':
    pprint.pprint( get_config() )
