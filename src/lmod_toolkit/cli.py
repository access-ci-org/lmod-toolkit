import argparse
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

def main():
    args = get_args()
    if args.action == 'test':
        lmtk.test
    elif args.action == 'publish':
        print( "PUBLISH" )
    elif args.action == 'mkcfg':
        print( "MKCFG" )
    else:
        raise UserWarning( f"Unknown or invalid action: '{args.action}'" )
