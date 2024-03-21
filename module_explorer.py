"""
Module Explorer v0.2.0
Requires one arg: module name.
Prints out lots of info about the module including comments from it's author.
It's no pydoc but it's fun to work on. Would be nice to have a Qt GUI!
"""

import sys
import importlib
import inspect
import types

VERSION = "v0.2.0"

def main(args: list):
    """main"""
    try:
        module_name = args[1].split(".")[0]  # remove suffix and discard it
    except IndexError:
        print(f"Module Explorer {VERSION}\n view documentation directly from python modules")
        print(f"\nUsage: python {sys.argv[0]} <module>[.py|.pyi] | <package>")
        sys.exit(0)

    # try to import the module we want to inspect.
    # h/t to https://stackoverflow.com/questions/301134
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        print(f"Can't import {args[1]}! Bailing!")
        sys.exit(0)

    # get all of it's member objects
    module_members_list = inspect.getmembers(module)

    # print header
    header_str = f"\t\t\t{module.__name__}\n\n{inspect.getdoc(module)}\n"
    print(header_str)

    # go through the members list of tuples and get the info we want
    for object_name, object_type in module_members_list:
        if object_name.find("__") >= 0:
            continue  # skip dunders: need to learn more about this
        if isinstance(object_type, (int, str, types.ModuleType)) is True:
            continue # skip int and str constants, and child modules
        if (
            inspect.isfunction(object_type) is True
            or inspect.isbuiltin(object_type) is True
            or inspect.ismethod(object_type) is True
        ):
            s = inspect.Signature.from_callable(object_type)
            sig = s.from_callable(object_type)
            if sig:
                print(f"NAME:\t {object_name}{sig}")
            else:
                print("NAME:\t {object_name}()")

            print("TYPE:\t function")
        else:
            print("NAME:\t", object_name)
            print("TYPE:\t", object_type)

        if object_type.__doc__ is None:
            print("DOCS:\tUndocumented")
        else:
            print("DOCS:\t", object_type.__doc__.strip())
        print("\n\n")


if __name__ == "__main__":
    main(sys.argv)
