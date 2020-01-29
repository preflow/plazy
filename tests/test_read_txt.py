# -*- coding: utf-8 -*-
import plazy
import os
import shutil


def test_read_txt():
    # create root dir
    test_dirname = "_test_"
    os.makedirs(test_dirname) if not os.path.isdir(test_dirname) else None

    # dummy txt content
    txt_content = [
        "1.jpg,3,person,0.4,0.5,0.6,0.7",
        "  2.jpg,3,person,0.4,0.5,0.6,0.7   ",
        "\t\t 3.jpeg,3,person,0.4,0.5,0.6,0.9 \t ",
        " ",
    ]
    dummy_file = os.path.join(test_dirname, "dummy.txt")
    with open(dummy_file, "w") as f:
        f.write("\n".join(txt_content))

    lines = plazy.read_txt(path=dummy_file)
    # clean
    shutil.rmtree(test_dirname)

    assert len(lines) == 3
    assert len(lines[0]) == len(txt_content[0])
    assert lines[1].startswith("2.jpg")
    assert lines[1].endswith("0.7")
    assert lines[2].startswith("3.jpeg")
    assert lines[2].endswith("0.9")
    pass
