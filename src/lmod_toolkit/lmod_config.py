import json
import subprocess
import pprint
import functools

__all__ = [
    'Lmod_Config',
]

class Lmod_Config :
    def __init__( self ):
        self.raw = None
        self.config = None
        self._load()

    def _load( self ):
        cmds = [ 'bash', '-l', '-c', 'module --config_json' ]
        result = subprocess.run(
            cmds,
            capture_output=True,  # Captures both stdout and stderr
            text=True             # Returns strings instead of bytes
        )
        # pprint.pprint( ['STDOUT', result.stdout] )
        # pprint.pprint( ['STDERR', result.stderr] )
        self.config = json.loads( result.stderr )

    @functools.cached_property
    def get_key( self, key ):
        return self.config[ key ]


if __name__ == '__main__':
    lmc = Lmod_Config()
    pprint.pprint( lmc.config )
