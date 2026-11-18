import functools
import json
import pprint
import re

from pathlib import Path

import lmod_toolkit as lmtk

__all__ = [
    'as_json',
    'get_ext_attrs',
    ]

# Adapted from:
# https://github.com/access-ci-org/ipf/blob/3e419ebb2d0f404454ec7a8c3630f5cf24c2d756/ipf/glue2/modules.py#L444
EXTATTR_KEYS = [
    'Name',
    'Version',
    '.*escription',
    'URL',
    'Category',
    'Keywords',
    'SupportStatus',
    'SupportContact',
    'Default',
    'IPF_FLAGS',
    ]
LONGEST_FIRST = sorted(EXTATTR_KEYS, key=len, reverse=True)
WHATIS_RE = re.compile(r'whatis\(\[\[((?:{}))\s*:\s*(.*)\]\]\)'.format('|'.join(LONGEST_FIRST)))
COMMENT_RE = re.compile(r'\"((?:{})):([^\"]+)\"'.format('|'.join(LONGEST_FIRST)))


def get_ext_attrs():
    ''' Search through all modules' lua files for any extended attributes.
        Extended attributes are non-lmod supported data added to a lua file.
    '''
    ext_attrs = {}
    for module in lmtk.lmod_spider.get_module_data():
        for version in module[ 'versions' ]:
            path = version[ 'path' ]
            # skip non-lua files
            if not path.endswith(".lua"):
                #logr.debug( f"skipping non-lua file {path}" )
                print( f"skipping non-lua file {path}" )
                continue
            filepath = Path( path )
            try:
                file_contents = filepath.read_text()
            except ( FileNotFoundError, PermissionError, IOError ) as e:
                #logr.debug( f"error opening file '{filepath}' {e}" )
                print( f"error opening file '{filepath}' {e}" )
                continue
            ext_data = get_ext_attrs_from_lua_file( file_contents )
            if ext_data:
                full_name = version[ 'full' ]
                ext_attrs[ full_name ] = ext_data
    return ext_attrs


# wrapping this with functools.cache ensures we open a file only once
@functools.cache
def get_ext_attrs_from_lua_file( text: str ) -> dict:
    ''' text parsing taken from
        https://github.com/access-ci-org/ipf/blob/3e419ebb/ipf/glue2/modules.py#L444
    '''
    whatis_res = WHATIS_RE.findall(text)
    comment_res = COMMENT_RE.findall(text)
    # Return all tuples found, allow "comment" to override "whatis"
    ext_attrs = {
        k: v
        for k, v in whatis_res+comment_res
        }
    return ext_attrs


def as_dict():
    return get_ext_attrs()


def as_json():
    return json.dumps( as_dict() )


if __name__ == '__main__':
    pprint.pprint( get_ext_attrs() )
