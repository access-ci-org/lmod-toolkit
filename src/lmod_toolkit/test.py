
import lmod_toolkit as lmtk

print( '\nLMOD CONFIG' )
print(   '===========' )
print( lmtk.lmod_config.as_json() )

print( '\nLMOD SPIDER' )
print(   '===========' )
print( lmtk.lmod_spider.as_json() )

print( '\nLMOD EXT ATTRS' )
print(   '==============' )
print( lmtk.lmod_ext_attrs.as_json() )
