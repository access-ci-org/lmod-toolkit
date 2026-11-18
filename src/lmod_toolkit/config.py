import os
from pathlib import Path
from platformdirs import PlatformDirs

import lmod_toolkit as lmtk


__all__ = [
    'get_config_path',
    'get_config',
    'mk_config',
]

@functools.cache
def get_config_path():
    # allow LMTK_CONFIG_PATH override
    from_env = os.getenv( 'LMTK_CONFIG_PATH', None ) #default to None
    if from_env:
        cfg_path = Path( from_env )
    else:
        dirs = PlatformDirs( appname=__package__, ensure_exists=True )
        cfg_path = dirs.place_config_file( "common.toml" )
    return cfg_path


@functools.cache
def get_config():
    cfg_path = get_config_path()
    with cfg_path.open( mode='rb' ) as fh:
        cfg_data = tomllib.load( fh )
    return cfg_data


def mk_config():
    cfg_path = get_config_path()
    if cfg_path.exists():
        raise UserWarning( f"ConfigFile '{cfg_path}' exists, refusing to overwrite" )
    # get module install dir
    pkg_dir = lmtk.install_path
    cfg_sample = pkg_dir / 'conf' / 'config.toml.sample'
    encoding='utf-8'
    sample_text = cfg_sample.read_text( encoding=encoding )
    cfg_path.write_test( sample_text, encoding=encoding )
