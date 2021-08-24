# -*- coding: utf-8 -*-
import plazy


class Person(object):
    def __init__(self, name):
        self.name = name


def test_setattr_from_dict_default():
    p = Person(name="plazy")
    new_name = "yzalp"
    new_age = 28
    d = {
        "name": new_name,
        "age": new_age,
    }
    plazy.setattr_from_dict(obj=p, kv=d)
    assert p.name == new_name
    assert hasattr(p, "age")
    assert p.age == new_age


def test_setattr_from_dict_override():
    pname = "plazy"
    p = Person(name=pname)
    new_name = "yzalp"
    new_age = 28
    d = {
        "name": new_name,
        "age": new_age,
    }
    plazy.setattr_from_dict(obj=p, kv=d, override=False)
    assert p.name != new_name and p.name == pname  # because "override" is set to False
    assert hasattr(p, "age")
    assert p.age == new_age
