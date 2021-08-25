# -*- coding: utf-8 -*-
import copy
import sys
from functools import wraps
import inspect

# random_string()
import string
import random

# ----------------------
# | Internal functions |
# ----------------------


def _set_original_func(func, original_func, override=False):
    if hasattr(func, "__o_func") and not override:
        return
    func.__o_func = original_func


def _get_original_func(func):
    if hasattr(func, "__o_func"):
        return getattr(func, "__o_func")
    else:
        return None


def _get_arg_spec(x):
    target_x = _get_original_func(x)
    target_x = x if not target_x else target_x
    major, minor, micro, _, _ = sys.version_info
    if major == 2:
        names, varargs, keywords, defaults = inspect.getargspec(target_x)
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
        ) = inspect.getfullargspec(target_x)
    return names, varargs, keywords, defaults


# ----------------------


def setattr_from_dict(obj, kv, override=True):
    for k, v in kv.items():
        if hasattr(obj, k) and not override:
            continue
        setattr(obj, k, v)
    return obj


def random_string(size=6, digit=True, lower=True, upper=True):
    # ref: https://stackoverflow.com/a/2257449
    assert (digit or lower or upper) is True
    chars = []
    chars += string.digits if digit else []
    chars += string.ascii_lowercase if lower else []
    chars += string.ascii_uppercase if upper else []
    return "".join(random.choice(chars) for _ in range(size))


# --------------
# | Decorators |
# --------------


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
    Reference: https://stackoverflow.com/a/1389216
    """

    names, varargs, keywords, defaults = _get_arg_spec(func)

    @wraps(func)
    def wrapper(self, *args, **kargs):
        argnames = names[1:]
        unexpected_argnames = [key for key in kargs.keys() if key not in argnames]
        if len(argnames) < len(args):
            func(self, *args, **kargs)  # will raise error

        for name, arg in list(zip(argnames, args)) + list(kargs.items()):
            setattr(self, name, arg)

        default_values = [] if defaults is None else defaults
        for name, default_val in zip(reversed(argnames), reversed(default_values)):
            if not hasattr(self, name):
                setattr(self, name, default_val)

        # remove unexpected args
        for key in unexpected_argnames:
            kargs.pop(key, None)

        func(self, *args, **kargs)

    _set_original_func(wrapper, func)

    return wrapper


def auto_assign_strict(func):
    """
    Automatically assigns the parameters.

    >>> class process:
    ...     @auto_assign
    ...     def __init__(self, cmd, reachable=False, user='root'):
    ...         pass
    >>> p = process('halt', True)
    >>> p.cmd, p.reachable, p.user
    ('halt', True, 'root')
    Reference: https://stackoverflow.com/a/1389216
    """

    names, varargs, keywords, defaults = _get_arg_spec(func)

    @wraps(func)
    def wrapper(self, *args, **kargs):
        argnames = names[1:]
        unexpected_argnames = [key for key in kargs.keys() if key not in argnames]
        if len(argnames) < len(args) or len(unexpected_argnames) > 0:
            func(self, *args, **kargs)  # will raise error

        for name, arg in list(zip(argnames, args)) + list(kargs.items()):
            setattr(self, name, arg)

        default_values = [] if defaults is None else defaults
        for name, default_val in zip(reversed(argnames), reversed(default_values)):
            if not hasattr(self, name):
                setattr(self, name, default_val)

        func(self, *args, **kargs)

    _set_original_func(wrapper, func)

    return wrapper


def cloneable(func):

    names, varargs, keywords, defaults = _get_arg_spec(func)

    @wraps(func)
    def wrapper(self, *args, **kargs):
        argnames = names[1:]
        _kw = {}
        for name, arg in list(zip(argnames, args)) + list(kargs.items()):
            _kw[name] = arg

        # # set default values to _kw?! does it need?
        # default_values = [] if defaults is None else defaults
        # for name, default_val in zip(reversed(argnames), reversed(default_values)):
        #     if not hasattr(self, name):
        #         _kw[name] = default_val

        _kw = copy.deepcopy(_kw)

        func(self, *args, **kargs)

        def func_clone(*c_args, **c_kargs):
            kw_copy = copy.deepcopy(_kw)
            for name, arg in list(zip(argnames, c_args)) + list(c_kargs.items()):
                kw_copy[name] = arg
            return self.__class__(**kw_copy)

        self.clone = func_clone

    _set_original_func(wrapper, func)

    return wrapper


# --------------
