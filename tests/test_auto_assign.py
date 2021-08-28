# -*- coding: utf-8 -*-
import plazy
from scake import Scake


class CStrict(object):
    @plazy.auto_assign_strict
    def __init__(self, a, b, c=15):
        pass


class CMixParams(object):
    @plazy.auto_assign
    def __init__(self, a, b, c=100, d="Minh"):
        pass

    def __call__(self):
        self.e = True


class CFullRequiredParams(object):
    @plazy.auto_assign
    def __init__(self, a, b, c):
        pass


class CFullDefault(object):
    @plazy.auto_assign
    def __init__(self, a=1, b="b", c=None):
        pass

    def __call__(self):
        self.e = True


class CNoArg(object):
    @plazy.auto_assign
    def __init__(self):
        self.me = 10
        pass


def test_auto_assign_exceed_params():
    try:
        CMixParams(10, 20, 30, 40, 50)
        assert False
    except Exception:
        assert True


def test_auto_assign_strict_successful():
    x = CStrict(10, 20)
    assert x.a == 10
    assert x.b == 20
    assert x.c == 15


def test_auto_assign_strict_failed():
    try:
        CStrict(10, 20, d=30)
        assert False
    except Exception:
        assert True


def test_auto_assign_colab_with_scake_ref():
    config = {
        "other_class": {"$CFullDefault": {"a": 100, "b": 110}},
        "dummy_class": {
            "$CFullDefault": {"a": 200, "b": "=/other_class", "c": 1000},
            "run():": "__call__",
        },
    }
    s = Scake(config, class_mapping=globals())
    s.run(debug=True)
    assert True
    x = s["/dummy_class"]
    assert x.a == 200
    assert x.b.a == 100 and x.b.b == 110
    assert x.c == 1000


def test_auto_assign_colab_with_scake():
    config = {
        "dummy_class": {
            "$CFullDefault": {"a": 200, "b": 500, "c": 1000},
            "run():": "__call__",
        },
    }
    s = Scake(config, class_mapping=globals())
    s.run(debug=True)
    assert True
    x = s["/dummy_class"]
    assert x.a == 200
    assert x.b == 500
    assert x.c == 1000


def test_auto_assign_passing_list_params():
    params = [20, 50, 100, "test"]
    x = CMixParams(*params)
    assert x.a == 20
    assert x.b == 50
    assert x.c == 100
    assert x.d == "test"


def test_auto_assign_passing_dict_params():
    params = {
        "b": 50,
        "a": 20,
        "d": "test",
    }
    x = CMixParams(**params)
    assert x.a == 20
    assert x.b == 50
    assert x.c == 100
    assert x.d == "test"


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
