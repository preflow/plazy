# -*- coding: utf-8 -*-
import re
import plazy

# https://stackoverflow.com/a/11232512


def _contains_digits(d):
    _digits = re.compile(r"\d")
    return bool(_digits.search(d))


def test_random_string():
    rstring = plazy.random_string()  # iVr3FY
    assert type(rstring) is str


def test_random_string_length():
    rstring = plazy.random_string(size=8)  # XqVDuu5R
    assert type(rstring) is str
    assert len(rstring) == 8


def test_random_string_digit_only():
    rstring = plazy.random_string(
        size=6, digit=True, lower=False, upper=False
    )  # 763099
    assert type(rstring) is str
    assert len(rstring) == 6
    assert rstring.isdigit()


def test_random_string_lower_only():
    rstring = plazy.random_string(
        size=6, digit=False, lower=True, upper=False
    )  # djzcch
    assert type(rstring) is str
    assert len(rstring) == 6
    assert _contains_digits(rstring) is False
    assert rstring.lower() == rstring


def test_random_string_upper_only():
    rstring = plazy.random_string(
        size=6, digit=False, lower=False, upper=True
    )  # BGBMQN
    assert type(rstring) is str
    assert len(rstring) == 6
    assert _contains_digits(rstring) is False
    assert rstring.upper() == rstring
