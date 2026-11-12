import functools
import json
import pprint
import subprocess

__all__ = [
    'as_json',
    'get_config',
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


def as_json():
    return json.dumps( get_config() )


def __getattr__( name ):
    cfg = get_config()
    try:
        val = cfg['configT'][name]
    except KeyError as e:
        raise AttributeError( f"'{name}' not found" )
    return val


if __name__ == '__main__':
    pprint.pprint( get_config() )
