# -*- coding: utf-8 -*-
import plazy


def test_b64encode_pretty():
    my_string = "plazy"
    e_string = plazy.b64encode(my_string, pretty=True)
    assert type(my_string) is str
    assert type(e_string) is str
    assert not e_string.endswith("=")


def test_b64encode():
    my_string = "plazy"
    e_string = plazy.b64encode(my_string)
    assert type(my_string) is str
    assert type(e_string) is str


def test_b64decode():
    my_string = "plazy"
    result = plazy.b64decode(plazy.b64encode(my_string))
    assert type(my_string) is str
    assert type(result) is str
    assert result == my_string
