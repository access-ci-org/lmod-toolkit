import pprint
from textwrap import dedent
from tomllib import TOMLDecodeError

import lmod_toolkit as lmtk


def lmtk_config_test():
    print( '\nLmod-toolkit Config' )
    print(   '===================' )
    try:
        cfg = lmtk.config.get_config()
    except TOMLDecodeError as e:
        msg = dedent( f"""
            Error parsing config file '{lmtk.config.get_config_path()}'
            tomllib.TOMLDecodeError ({e})
            """).strip( "\n" )
        raise SystemExit( msg )
    else:
        pprint.pprint( cfg )


def lmod_config_test():
    print( '\nLMOD CONFIG' )
    print(   '===========' )
    print( lmtk.lmod_config.as_json() )


def lmod_spider_test():
    print( '\nLMOD SPIDER' )
    print(   '===========' )
    print( lmtk.lmod_spider.as_json() )


def lmod_extended_attrs_test():
    print( '\nLMOD EXT ATTRS' )
    print(   '==============' )
    print( lmtk.lmod_ext_attrs.as_json() )



def all_tests():
    lmtk_config_test() #test loading the config

    # initialize config by loading the first resource
    resources = lmtk.config.iter_resources() #iter_resources is a generator function
    next( resources ) #tell the generator to "set up" the first resource

    lmod_config_test()
    lmod_spider_test()
    lmod_extended_attrs_test()

if __name__ == '__main__':
    all_tests()
