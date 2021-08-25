# -*- coding: utf-8 -*-
import plazy


class Foo(object):
    @plazy.cloneable
    def __init__(self, a, b):
        self.a = a
        self.b = b
        pass


class Bar(object):
    @plazy.cloneable
    @plazy.auto_assign
    def __init__(self, a, b, c=10):
        pass


def test_clone_1():
    f = Foo(1, 2)
    f1 = f.clone(3, 4)
    f2 = f.clone(5)
    f3 = f.clone(a=10, b=20)
    f4 = f.clone(b=30)
    assert f1.a == 3
    assert f1.b == 4
    assert f2.a == 5
    assert f2.b == 2
    assert f3.a == 10
    assert f3.b == 20
    assert f4.a == 1
    assert f4.b == 30
    pass


def test_clone_2():
    x = Foo(1, 2)
    x1 = x.clone(3, 4)
    y = Foo(50, 60)
    y1 = y.clone(35, 36)
    z = Foo(120, 210)
    z1 = z.clone("za", "zb")
    z2 = z.clone(b="zz")
    y2 = y.clone(-1)
    assert x1.a == 3 and x1.b == 4
    assert y1.a == 35 and y1.b == 36
    assert z1.a == "za" and z1.b == "zb"
    assert z2.a == 120 and z2.b == "zz"
    assert y2.a == -1 and y2.b == 60


def test_clone_3():
    f = Bar(1, 2)
    f1 = f.clone(3, 4)
    f2 = f.clone(5)
    f3 = f.clone(a=10, b=20)
    f4 = f.clone(b=30)
    f5 = f.clone()
    assert f.a == 1
    assert f.b == 2
    assert f1.a == 3
    assert f1.b == 4
    assert f2.a == 5
    assert f2.b == 2
    assert f3.a == 10
    assert f3.b == 20
    assert f4.a == 1
    assert f4.b == 30
    assert f5.a == 1
    assert f5.b == 2
    pass


def test_clone_4():
    x = Bar(1, 2)
    x1 = x.clone(3, 4)
    y = Foo(50, 60)
    y1 = y.clone(35, 36)
    z = Foo(120, 210)
    z1 = z.clone("za", "zb")
    z2 = z.clone(b="zz")
    y2 = y.clone(-1)
    assert x1.a == 3 and x1.b == 4
    assert y1.a == 35 and y1.b == 36
    assert z1.a == "za" and z1.b == "zb"
    assert z2.a == 120 and z2.b == "zz"
    assert y2.a == -1 and y2.b == 60


def test_clone_5():
    barclub = Bar(1, 2, d=3)
    bc1 = barclub.clone(b=-2)
    bc2 = barclub.clone(e=4)
    bc3 = barclub.clone()
    bc4 = barclub.clone(a=10, b=20, c=30, d=40, e=50)
    assert bc1.a == 1 and bc1.b == -2 and bc1.c == 10 and bc1.d == 3
    assert bc2.a == 1 and bc2.b == 2 and bc2.c == 10 and bc2.d == 3 and bc2.e == 4
    assert bc3.a == 1 and bc3.b == 2 and bc3.c == 10 and bc3.d == 3
    assert bc4.a == 10 and bc4.b == 20 and bc4.c == 30 and bc4.d == 40 and bc4.e == 50
