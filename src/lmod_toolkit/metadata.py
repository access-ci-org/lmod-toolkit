import functools
import importlib.metadata
import json
import pathlib
import pprint

import lmod_toolkit as lmtk

__all__ = [
    'as_json',
    'get_metadata',
]


@functools.cache
def get_metadata():
    {
        __package__: {
            'version': importlib.metadata.version( __package__ ),
            'install_path': pathlib.Path(__file__).resolve().parent(),
        }
    }


def as_json():
    return json.dumps( get_metadata() )


def __getattr__( name ):
    return( get_metadata()[__package__][name] )

if __name__ == '__main__':
    pprint.pprint( get_config() )
