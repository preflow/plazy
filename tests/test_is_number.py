# -*- coding: utf-8 -*-
import plazy


def test_is_number_int():
    s = "1"
    assert plazy.is_number(s) is True


def test_is_number_float():
    s = "0.234"
    assert plazy.is_number(s) is True


def test_is_number_neg():
    s = "-0.234"
    assert plazy.is_number(s) is True


def test_is_number_e():
    s = "1e3"
    assert plazy.is_number(s) is True


def test_is_number_not_number_1():
    s = "plazy"
    assert plazy.is_number(s) is False


def test_is_number_not_number_2():
    s = "1.23k9"
    assert plazy.is_number(s) is False


def test_is_number_not_number_3():
    s = "x.3253254"
    assert plazy.is_number(s) is False
