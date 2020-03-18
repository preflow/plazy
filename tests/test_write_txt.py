# -*- coding: utf-8 -*-
import plazy
import os
import shutil

TXT_CONTENT = [
    "welcome",
    "to",
    "plazy!",
]


def test_write_txt_default():
    # init
    test_dirname = "_test_"
    os.makedirs(test_dirname) if not os.path.isdir(test_dirname) else None
    dummy_file = os.path.join(test_dirname, "dummy_%s.txt" % (plazy.random_string()))

    plazy.write_txt(path=dummy_file, lines=TXT_CONTENT)
    with open(dummy_file, "r") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    # clean
    shutil.rmtree(test_dirname)

    assert lines == TXT_CONTENT


def test_write_txt_cat_str():
    # init
    test_dirname = "_test_"
    os.makedirs(test_dirname) if not os.path.isdir(test_dirname) else None
    dummy_file = os.path.join(test_dirname, "dummy_%s.txt" % (plazy.random_string()))

    cstr = ","
    plazy.write_txt(path=dummy_file, lines=TXT_CONTENT, cat_str=cstr)
    with open(dummy_file, "r") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    # clean
    shutil.rmtree(test_dirname)

    assert lines[0] == cstr.join(TXT_CONTENT)
