# -*- coding: utf-8 -*-
import plazy
import os
import shutil


def test_list_files():
    # create root dir
    test_dirname = "_test_"
    os.makedirs(test_dirname, exist_ok=True)

    # create sub dir
    test_subdir = "_sub_"
    test_subdir_full = os.path.join(test_dirname, test_subdir)
    os.makedirs(test_subdir_full, exist_ok=True)

    # create dummy files in _test_
    test_files = ["1.jpg", "2.jpg", "3.jpeg"]
    for tf in test_files:
        with open(os.path.join(test_dirname, tf), "w") as f:
            f.write("hello")

    # create dummy files in _test_/_sub_
    test_file_in_subdir = os.path.join(test_subdir_full, "4.jpg")
    with open(test_file_in_subdir, "w") as f:
        f.write("hello")

    result = plazy.list_files(
        root=test_dirname,
        filter_func=lambda x: True if x.endswith(".jpg") else False,
        is_include_root=False,
    )
    # clean
    shutil.rmtree(test_dirname)

    assert isinstance(result, (tuple, list))
    assert len(result) == 3
    assert "1.jpg" in result
    assert "2.jpg" in result
    assert "_sub_/4.jpg" in result
    pass
