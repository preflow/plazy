# -*- coding: utf-8 -*-
import plazy


class CMixParams(object):
    @plazy.auto_assign
    def __init__(self, a, b, c=100, d="Minh"):
        pass


class CFullRequiredParams(object):
    @plazy.auto_assign
    def __init__(self, a, b, c):
        pass


class CFullDefault(object):
    @plazy.auto_assign
    def __init__(self, a=1, b="b", c=None):
        pass


class CNoArg(object):
    @plazy.auto_assign
    def __init__(self):
        self.me = 10
        pass


def test_auto_assign_missing_required_param():
    try:
        CMixParams(70)
        assert False
    except Exception as e:
        print(e)
        assert True
    pass


def test_auto_assign_mix_params():
    x = CMixParams(b=50, a=20, d="test")
    assert x.a == 20
    assert x.b == 50
    assert x.c == 100
    assert x.d == "test"


def test_auto_assign_required_params():
    x = CFullRequiredParams(1, 2, 3)
    assert x.a == 1
    assert x.b == 2
    assert x.c == 3


def test_auto_assign_full_default_args():
    x = CFullDefault()
    assert x.a == 1
    assert x.b == "b"
    assert x.c is None


def test_auto_assign_no_arg():
    x = CNoArg()
    assert x.me == 10
