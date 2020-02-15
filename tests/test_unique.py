# -*- coding: utf-8 -*-
import plazy


def test_unique_tuple_sort_reverse():
    sample = (7, 3, 5, 3, 3, 7, 9)
    u_sample = plazy.unique(seq=sample, sort=True, reverse=True)
    assert u_sample == (9, 7, 5, 3)


def test_unique_tuple_sort():
    sample = (7, 3, 5, 3, 3, 7, 9)
    u_sample = plazy.unique(seq=sample, sort=True)
    assert u_sample == (3, 5, 7, 9)


def test_unique_list():
    sample = [7, 3, 5, 3, 3, 7, 9]
    u_sample = plazy.unique(seq=sample)
    assert u_sample == [7, 3, 5, 9]


def test_unique_tuple():
    sample = (7, 3, 5, 3, 3, 7, 9)
    u_sample = plazy.unique(seq=sample)
    assert u_sample == (7, 3, 5, 9)


def test_already_unique_list():
    sample = [2, 7, 9, 1]
    u_sample = plazy.unique(seq=sample)
    assert u_sample == sample


def test_already_unique_tuple():
    sample = (2, 7, 9, 1)
    u_sample = plazy.unique(seq=sample)
    assert u_sample == sample
