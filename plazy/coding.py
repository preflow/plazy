# -*- coding: utf-8 -*-
import sys
from functools import wraps
import inspect
import os


def list_files(root, filter_func=None, is_include_root=False):
    assert os.path.isdir(root), "Invalid folder: %s" % root
    result = []
    for root_dir, sub_dir_list, files in os.walk(root):
        for f in files:
            fpath = os.path.join(root_dir, f)
            is_keep = filter_func(fpath) if filter_func else True
            if is_keep:
                if not is_include_root:
                    fpath = fpath.replace(root, "").strip("/")
                result.append(fpath)
            pass
        pass
    return result


# https://stackoverflow.com/a/1389216


def auto_assign(func):
    """
    Automatically assigns the parameters.

    >>> class process:
    ...     @auto_assign
    ...     def __init__(self, cmd, reachable=False, user='root'):
    ...         pass
    >>> p = process('halt', True)
    >>> p.cmd, p.reachable, p.user
    ('halt', True, 'root')
    """

    def _get_arg_spec(x):
        major, minor, micro, _, _ = sys.version_info
        if major == 2:
            names, varargs, keywords, defaults = inspect.getargspec(x)
        else:
            # https://docs.python.org/3.4/library/inspect.html#inspect.getfullargspec
            (
                names,
                varargs,
                keywords,
                defaults,
                kwonlyargs,
                kwonlydefaults,
                annotations,
            ) = inspect.getfullargspec(x)
        return names, varargs, keywords, defaults

    names, varargs, keywords, defaults = _get_arg_spec(func)

    @wraps(func)
    def wrapper(self, *args, **kargs):
        for name, arg in list(zip(names[1:], args)) + list(kargs.items()):
            setattr(self, name, arg)

        default_values = [] if defaults is None else defaults
        for name, default in zip(reversed(names), reversed(default_values)):
            if not hasattr(self, name):
                setattr(self, name, default)

        func(self, *args, **kargs)

    return wrapper
