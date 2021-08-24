# -*- coding: utf-8 -*-
import os


def write_txt(path, lines, mode="w", cat_str="\n"):
    """
    Write text file.
    """
    assert isinstance(lines, (tuple, list))
    if not lines:
        # do nothing, early quit!
        return
    with open(path, mode) as f:
        f.write(cat_str.join(lines))
    pass


def read_txt(path, line_func=None, skip_empty_line=False):
    """
    Read lines of text file as a list.
    """
    assert os.path.isfile(path), "plazy.read_txt @ path (%s) not found" % path
    with open(path, "r") as f:
        lines = f.readlines()
        lines = [line.rstrip("\n") for line in lines]
        if line_func is not None:
            lines = [line_func(line) for line in lines]
        if skip_empty_line:
            lines = [line for line in lines if len(line) > 0]
        return lines
    return []


def list_files(root="./", filter_func=None, is_include_root=False):
    assert os.path.isdir(root), "Invalid folder: %s" % root
    result = []
    for root_dir, sub_dir_list, files in os.walk(root):
        for f in files:
            fpath = os.path.join(root_dir, f)
            is_keep = filter_func(fpath) if filter_func else True
            if is_keep:
                if not is_include_root:
                    fpath = fpath.replace(root, "").strip("/")
                result.append(fpath)
            pass
        pass
    result = sorted(result)
    return result
