import argparse
from textwrap import dedent

import lmod_toolkit as lmtk


def get_args( params=None ):
    constructor_args = {
        'formatter_class': argparse.RawDescriptionHelpFormatter,
        'description': 'lmod_toolkit command line interface.',
        'epilog': '''NETRC:
            ACCESS lmod_toolkit publishing credentials should be stored in ~/.netrc.
            ''',
        }
    parser = argparse.ArgumentParser( **constructor_args )
    # parser.add_argument( '-d', '--debug', action='store_true' )
    # parser.add_argument( '-v', '--verbose', action='store_true' )
    action = parser.add_mutually_exclusive_group( required=True )
    action.add_argument( '--test',
        const='test',
        dest='action',
        action='store_const',
        help='Test run of gathering publishing data' )
    action.add_argument( '--mkcfg',
        const='mkcfg',
        dest='action',
        action='store_const',
        help='Copy a sample config into the default location' )
    action.add_argument( '--publish',
        const='publish',
        dest='action',
        action='store_const',
        help='Collect and publish data (default)' )
    # parser.set_defaults(
    #     action = 'publish',
    # )
    args = parser.parse_args( params )
    return args


def mkcfg():
    try:
        lmtk.config.mk_config()
    except UserWarning as e:
        msg = str( e )
    else:
        msg = dedent( f"""
            New config file: '{lmtk.config.get_config()}'
            You MUST add at least one valid resource to the config before publishing.
            Next Steps:
              1. Edit the config file '{lmtk.config.get_config()}'
              2. Test with: '~/lmod-toolkit/bin/python -m lmod_toolkit --test'
        """).strip( "\n" )
    return( msg )


def main():
    args = get_args()
    if args.action == 'test':
        lmtk.test.all_tests()
    elif args.action == 'publish':
        lmtk.publish.go()
    elif args.action == 'mkcfg':
        status = mkcfg()
        print( status )
    else:
        raise SystemExit( f"Invalid action: '{args.action}'" )
