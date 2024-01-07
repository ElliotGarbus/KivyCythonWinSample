from types import MappingProxyType
from mylibrary.subdir import constants

_STATIC_STORE = []

def _make_constants_map():
    output = {}
    for key in dir(constants):
        if key.startswith("constant_"):
            output[key] = getattr(constants, key)
    _STATIC_STORE.append(output)
    return MappingProxyType(output)

MyLib_Constants = _make_constants_map()