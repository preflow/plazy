# -*- coding: utf-8 -*-
import plazy
import os
import shutil

TXT_CONTENT = [
    "1.jpg,3,person,0.4,0.5,0.6,0.7",
    "  2.jpg,3,person,0.4,0.5,0.6,0.7   ",
    "\t\t 3.jpeg,3,person,0.4,0.5,0.6,0.9 \t ",
    " ",
]


def test_read_txt():
    # create root dir
    test_dirname = "_test_"
    os.makedirs(test_dirname) if not os.path.isdir(test_dirname) else None
    dummy_file = os.path.join(test_dirname, "dummy.txt")
    with open(dummy_file, "w") as f:
        f.write("\n".join(TXT_CONTENT))

    lines = plazy.read_txt(path=dummy_file, line_func=None)
    # clean
    shutil.rmtree(test_dirname)

    assert lines == TXT_CONTENT
    pass


def test_read_txt_line_func_no_remove_empty():
    # create root dir
    test_dirname = "_test_"
    os.makedirs(test_dirname) if not os.path.isdir(test_dirname) else None
    dummy_file = os.path.join(test_dirname, "dummy.txt")
    with open(dummy_file, "w") as f:
        f.write("\n".join(TXT_CONTENT))

    lines = plazy.read_txt(
        path=dummy_file, line_func=lambda x: x.strip(), skip_empty_line=False
    )
    # clean
    shutil.rmtree(test_dirname)

    assert len(lines) == 4
    assert len(lines[0]) == len(TXT_CONTENT[0])
    assert lines[1].startswith("2.jpg")
    assert lines[1].endswith("0.7")
    assert lines[2].startswith("3.jpeg")
    assert lines[2].endswith("0.9")
    pass


def test_read_txt_line_func_remove_empty():
    # create root dir
    test_dirname = "_test_"
    os.makedirs(test_dirname) if not os.path.isdir(test_dirname) else None
    dummy_file = os.path.join(test_dirname, "dummy.txt")
    with open(dummy_file, "w") as f:
        f.write("\n".join(TXT_CONTENT))

    lines = plazy.read_txt(
        path=dummy_file, line_func=lambda x: x.strip(), skip_empty_line=True
    )
    # clean
    shutil.rmtree(test_dirname)

    assert len(lines) == 3
    assert len(lines[0]) == len(TXT_CONTENT[0])
    assert lines[1].startswith("2.jpg")
    assert lines[1].endswith("0.7")
    assert lines[2].startswith("3.jpeg")
    assert lines[2].endswith("0.9")
    pass
