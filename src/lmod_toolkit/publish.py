import datetime
import importlib
import json
# import requests
import time

from pathlib import Path
from textwrap import dedent

import lmod_toolkit as lmtk


__all__ = [
    'get_resource_data',
]

data_functions = [
    'lmod_spider',
    'lmod_ext_attrs',
]


def go():
    lmtk_metadata = lmtk.metadata.as_dict()
    lmod_config_data = lmtk.lmod_config.as_dict()
    for resource_definition in lmtk.config.iter_resources():
        for pymod_name in data_functions:
            pymod = importlib.import_module( f"lmod_toolkit.{pymod_name}" )
            data_to_publish = {
                'resource': resource_definition,
                'lmod_toolkit': lmtk.metadata.as_dict(),
                'manifest': { 'data_type': pymod_name },
                'payload': pymod.as_dict(),
                }
            publish_data( data=data_to_publish, datatype=pymod_name )


def publish_data( data: dict, datatype: string ) -> None:
    filepath = write_to_local_file( data=data, datatype=datatype )
    # upload_http( data )


def write_to_local_file( data: dict, datatype: string ) -> Path:
    # make output filename
    ts = int( time.time() )
    timestamp = datetime.datetime.fromtimestamp( ts, tz=datetime.timezone.utc )
    fn_suffix = timestamp.strftime( '%F_%T%z' )
    outfile = lmtk.metadata.data_dir / f"{datatype}.{fn_suffix}"

    # write data
    with outfile.open( mode='w', encoding='utf-8' ) as fh:
        json.dump( data, fh )

    return outfile


def upload_http( filename: Path ) -> None:
    ''' Upload file data to a web API via HTTP.
        See also: https://github.com/andylytical/jira-tools/blob/main/web_api.py
    '''
    pass
