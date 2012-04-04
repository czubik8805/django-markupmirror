VERSION_INFO = {
    'major': 0,
    'minor': 1,
    'micro': 0,
    'sub': 'alpha',
    'serial': 0
}


def get_version(short=False):
    """Concatenates ``VERSION_INFO`` to dotted version string."""
    assert len(VERSION_INFO) == 5
    assert VERSION_INFO['sub'] in ('alpha', 'beta', 'candidate', 'final')

    version = "%(major)s.%(minor)s" % VERSION_INFO
    # append micro version only if not short and micro != 0
    if not short and VERSION_INFO['micro']:
        version += ".%(micro)s" % VERSION_INFO
    # append sub (pre-release) version and number
    if VERSION_INFO['sub'] != 'final':
        version += "%(sub)s%(serial)s" % VERSION_INFO
    return version


__version__ = get_version()
