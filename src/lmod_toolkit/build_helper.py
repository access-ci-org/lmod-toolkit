from setuptools_scm.version import ScmVersion, guess_next_version
import time

# import this module as part of build-system requires in pyproject.toml
# It must already exist on pypi as a published pkg for the build-system
# to be able to inlcude it...
# so for the very first time, use a different one (such as from ipf)
# in pyproject.toml, then once published, update pyproject.toml to use this one

def mk_version( version: ScmVersion ) -> str:
    # setuptools_scm template options
    # see also https://github.com/pypa/setuptools-scm/blob/main/setuptools-scm/src/setuptools_scm/version.py especially "def meta( ... )"
    # '{branch}',
    # '{dirty}',
    # '{distance}',
    # '{node}',
    # '{node_date}',
    # '{time}',
    # SPEACIAL NAMES
    # '{guessed}', #from version.py:format_next_version(...)

    final = 'unknown'
    if version.exact :
        final = version.format_with( '{tag}' )
    else :
        # unix timestamp as dev qualifier, ensures it's always unique
        # to comply with test.pypi.org requirement to NEVER re-use a version
        fmt_str = '{guessed}.dev' + str(int(time.time()))
        final = version.format_next_version( guess_next_version, fmt_str )
    return final
