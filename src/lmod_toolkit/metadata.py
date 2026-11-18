import functools
import importlib.metadata
import json
import pprint

from pathlib import Path

import lmod_toolkit as lmtk

__all__ = [
    'as_dict',
    'as_json',
]


@functools.cache
def get_metadata():
    pkg_install_dir = Path(__file__).resolve().parent
    user_install_dir = get_user_install_dir()
    data_dir = user_install_dir / 'data'
    log_dir = user_install_dir / 'logs'
    return {
        __package__: {
            'version': lmtk._version.version,
            'pkg_install_dir': pkg_install_dir,
			'user_install_dir': user_install_dir,
            'data_dir': data_dir,
            'log_dir': log_dir,
            }
        }


def get_user_install_dir():
    module_path = Path(__file__).resolve()
    parts = []
    for part in module_path.parts:
        if part != '.venv':
            parts.append( part )
        else:
            break
    return Path( *parts )


def as_dict():
    ''' Implement the common interface method as_dict()
        to get this module's relevant data as type dict
    '''
    return get_metadata()


def as_json():
    ''' Implement the common interface method as_json()
        to get this module's relevant data as a json string
    '''
    return json.dumps( get_metadata() )


def __getattr__( name ):
    return( get_metadata()[__package__][name] )

if __name__ == '__main__':
    pprint.pprint( as_json() )
