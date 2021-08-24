# -*- coding: utf-8 -*-
import sys
from functools import wraps
import inspect

# random_string()
import string
import random


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
