# -*- coding: utf-8 -*-
import sys
from functools import wraps
import inspect

import string
import random
import copy
import time


def random_string(size=6, digit=True, lower=True, upper=True):
    """
    Generate random string.

    Plazy version: 0.1.2+

    Parameters
    ----------
    size : int, optional
        Length of random string. Default: 6
    digit : bool, optional
        Random string may contains digits. Default: True
    lower : bool, optional
        Random string may contains lowercase letters. Default: True
    upper : bool, optional
        Random string may contains uppercase letters. Default: True

    Keyword Arguments
    -----------------

    Returns
    -------
    out : str
        Random string.

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 4,5,6,7,8,9

        import plazy

        if __name__ == "__main__":
            rstring = plazy.random_string() # iVr3FY
            rstring = plazy.random_string(upper=False) # mzvn7b
            rstring = plazy.random_string(size=8) # XqVDuu5R
            rstring = plazy.random_string(size=6, digit=True, lower=False, upper=False) # 763099
            rstring = plazy.random_string(size=6, digit=False, lower=True, upper=False) # djzcch
            rstring = plazy.random_string(size=6, digit=False, lower=False, upper=True) # BGBMQN

    See Also
    --------

    """
    # ref: https://stackoverflow.com/a/2257449
    assert (digit or lower or upper) is True
    chars = []
    chars += string.digits if digit else []
    chars += string.ascii_lowercase if lower else []
    chars += string.ascii_uppercase if upper else []
    return "".join(random.choice(chars) for _ in range(size))


class SingletonTimeStore:
    __instance = None

    @staticmethod
    def getInstance():
        """Static access method."""
        if SingletonTimeStore.__instance is None:
            SingletonTimeStore()
        return SingletonTimeStore.__instance

    def __init__(self):
        """Virtually private constructor."""
        if SingletonTimeStore.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SingletonTimeStore.__instance = self
        self.default_name = random_string()
        self.data = {}

    def set_time(self, name, value):
        self.data[name] = value

    def get_time(self, name, default=0):
        return self.data.get(name, default)

    def has_name(self, name):
        return name in self.data


g_time_store = SingletonTimeStore.getInstance()

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
    """
    Dynamically set object attributes from dictionary at runtime

    Plazy version: 0.1.4+

    Parameters
    ----------
    obj : object
        Object to set attributes on
    kv : dict
        Dictionary of key-value pairs to set
    override : bool, optional
        Whether to override existing attributes. Default: True

    Returns
    -------
    out : object
        Object with attributes set

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 10,11,12,19,20,21,22,23,24

        import plazy

        # Our custom class
        class Person(object):
            def __init__(self, name):
                self.name = name

        if __name__ == "__main__":
            p1 = Person(name="plazy") # init a Person object
            plazy.setattr_from_dict(obj=p1, kv={
                "name": "yzalp",
                "age": 28,
            })
            print(p1.name) # "yzalp"
            print(p1.age)  # 28

            # set "override" to False
            p2 = Person(name="plazy") # init a Person object
            plazy.setattr_from_dict(obj=p2,
                                    override=False,
                                    kv={
                                        "name": "yzalp",
                                        "age": 28,
                                    })
            print(p1.name) # "plazy" <- no overriding the pre-existed attribute due to "override=False"
            print(p1.age)  # 28
    """
    for k, v in kv.items():
        if hasattr(obj, k) and not override:
            continue
        setattr(obj, k, v)
    return obj


def tic(*names):
    """
    Start timer, use `toc` to get elapsed time in seconds.

    Parameters
    ----------

    names : str, str, ...
        Names of timers

    Returns
    -------

    out : float
        Current timestamp

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 10,11,12

        import plazy

        def foo():
            total = 0
            for _ in range(100000):
                total += 1
            return total

        if __name__ == "__main__":
            plazy.tic()                 # T1
            plazy.tic("B")              # T2
            plazy.tic("C", "D", "E")    # T3
            foo()
            dt1 = plazy.toc()           # elapsed time since T1
            dt2 = plazy.toc("B")        # elapsed time since T2
            dt3 = plazy.toc("C", "D")   # elapsed time since T3
            foo()
            dt4 = plazy.toc("E")        # elapsed time since T3
            dt5 = plazy.toc("B")        # elapsed time since T2
            print(dt1)                  # 0.009924173355102539
            print(dt2)                  # 0.009925603866577148
            print(dt3)                  # [0.00992727279663086, 0.00992727279663086]
            print(dt4)                  # 0.020497798919677734
            print(dt5)                  # 0.020506620407104492

    See also
    --------
    toc

    """
    now_ts = time.time()
    name_arr = list(names) + (
        [
            g_time_store.default_name,
        ]
        if len(names) == 0
        else []
    )
    for n in name_arr:
        g_time_store.set_time(name=n, value=now_ts)
    return now_ts


def toc(*names, default=0):
    """
    Get elapsed time(s) from `tic`.

    Parameters
    ----------

    names : str...
        Names of timers

    Keyword Arguments
    -----------------

    default : float, optional
        Default value if name not found

    Returns
    -------

    out : float or list of float
        Elapsed time(s)

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 14,15,16,18,19

        import plazy

        def foo():
            total = 0
            for _ in range(100000):
                total += 1
            return total

        if __name__ == "__main__":
            plazy.tic()                 # T1
            plazy.tic("B")              # T2
            plazy.tic("C", "D", "E")    # T3
            foo()
            dt1 = plazy.toc()           # elapsed time since T1
            dt2 = plazy.toc("B")        # elapsed time since T2
            dt3 = plazy.toc("C", "D")   # elapsed time since T3
            foo()
            dt4 = plazy.toc("E")        # elapsed time since T3
            dt5 = plazy.toc("B")        # elapsed time since T2
            print(dt1)                  # 0.009924173355102539
            print(dt2)                  # 0.009925603866577148
            print(dt3)                  # [0.00992727279663086, 0.00992727279663086]
            print(dt4)                  # 0.020497798919677734
            print(dt5)                  # 0.020506620407104492

    See also
    --------
    tic

    """
    now_ts = time.time()
    name_arr = list(names) + (
        [
            g_time_store.default_name,
        ]
        if len(names) == 0
        else []
    )
    result = [
        (now_ts - g_time_store.get_time(name=n))
        if g_time_store.has_name(n)
        else default
        for n in name_arr
    ]
    if len(name_arr) <= 1:
        return result[0]
    else:
        return result


# --------------
# | Decorators |
# --------------


def auto_assign(func):
    """
    Assign attributes of class with the passed arguments automatically.

    Plazy version: 0.1.5+

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 4

        import plazy

        class Cat(object):
            @plazy.auto_assign
            def __init__(self, name, owner='Kyzas'):
                # no variable assignment needed
                pass

            def get_age(self):
                return self.age if hasattr(self, "age") else None

            def get_type(self):
                return self.type if hasattr(self, "type") else None

        if __name__ == "__main__":
            mydict = {"type": "pet"}
            my_cat = Cat('Kittie', age=10, **mydict) # "age" and "type" is unexpected arguments
            print(my_cat.name)          # Kittie
            print(my_cat.owner)         # Kyzas
            print(my_cat.get_age())     # 10
            print(my_cat.get_type())    # pet

    See Also
    --------
    auto_assign_strict
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
    Assign attributes of class with the passed arguments automatically,
    strictly check the parameters passed to the function.

    Plazy version: 0.1.5+

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 4

        import plazy

        class Cat(object):
            @plazy.auto_assign_strict
            def __init__(self, name, owner='Kyzas'):
                pass

        if __name__ == "__main__":
            my_cat = Cat('Kittie', 'Minh')
            print(my_cat.name)      # Kittie
            print(my_cat.owner)     # Minh
            his_cat = Cat('Lulu', 'Peter', 'Mary')  # TypeError
            her_cat = Cat('Kittie', age=10)         # TypeError

    See Also
    --------
    auto_assign
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
    """
    Mark constructor of class as being cloneable. Method `clone` is used to clone a new instance,
    its arguments are the same with the constructor.

    Plazy version: 0.1.5+

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 4,15,30,31,36,37

        import plazy

        class Cat(object):
            @plazy.cloneable
            def __init__(self, name, owner='Kyzas'):
                self.name = name
                self.owner = owner
                pass

            def get_info(self):
                return {"name": self.name, "owner": self.owner}

        class Dog(object):
            # combine auto_assign and cloneable decorators
            @plazy.cloneable
            @plazy.auto_assign
            def __init__(self, name, owner='Kyzas'):
                pass

            def get_info(self):
                result = {"name": self.name, "owner": self.owner}
                if hasattr(self, "age"):
                    result["age"] = self.age
                else:
                    result["age"] = -1
                return result

        if __name__ == "__main__":
            cat_template = Cat('<Cat Name>', '<Owner Name>')
            his_cat = cat_template.clone('Lulu', 'Peter')
            her_cat = cat_template.clone(name='Jessie')
            print(his_cat.get_info()) # {'name': 'Lulu', 'owner': 'Peter'}
            print(her_cat.get_info()) # {'name': 'Jessie', 'owner': '<Owner Name>'}

            dog_template = Dog(name="<Dog Name>", owner="<Owner Name>", age=10) # age=10 by default
            his_dog = dog_template.clone(owner='James')
            her_dog = dog_template.clone(name="Husky", owner="Bella", age=5, note="Super Cute")
            print(his_dog.get_info()) # {'name': '<Dog Name>', 'owner': 'James', 'age': 10}
            print(her_dog.get_info()) # {'name': 'Husky', 'owner': 'Bella', 'age': 5}
            print(her_dog.note)       # Super Cute

    """

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
