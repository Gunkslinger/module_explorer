""" Cheater's way of exploring modules. :-)
Requires one arg: module name.
Prints out lots of info about the module including comments from it's author
"""

import sys
import importlib
import inspect
import types



try:
    s = sys.argv[1].split(".")[0] # remove suffix and discard it
except IndexError:
    print("Module Explorer v 0.1\n view documentation directly from python modules")
    print(f"\nUsage: {sys.argv[0]} <module>[.py|.pyi]")
    sys.exit(0)

module_name = s  # remove suffix

# try to import the module we want to inspect.
# h/t to https://stackoverflow.com/questions/301134
# TODO: need to handle packages

try:
    module = importlib.import_module(module_name, package=None)
except ImportError:
    print(f"Can't import {module_name}! Bailing!")
    sys.exit(0)

# get all of it's member objects
module_members = inspect.getmembers(module)

# print header
header = f"\t\t\t{module.__name__}\n\n{inspect.getdoc(module)}\n"
print(header)

# go through the members list of tuples and get the info we want
for module_name, module_type in module_members:
    if module_name.find("__") >= 0:  # skip dunders
        continue
    if (
        isinstance(
            module_type,  # skip int and str vars, and child modules
            (int, str, types.ModuleType),
        )
        is True
    ):
        continue
    print("NAME:\t", module_name)
    print("TYPE:\t", module_type)
    if module_type.__doc__ is None:
        print("DOCS:\tUndocumented")
    else:
        print("DOCS:\t", module_type.__doc__)
    print("\n\n")
