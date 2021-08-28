# -*- coding: utf-8 -*-
import os


def write_txt(path, lines, mode="w", cat_str="\n"):
    """
    Write text file from list.

    Plazy version: 0.1.4+

    Parameters
    ----------
    path : str
        Path text file to write.
    lines : list or tuple
        Sequence of lines (string) to write.
    mode : str, optional
        Write mode. Default: "w". Supported modes: https://docs.python.org/3/library/functions.html?highlight=open#open
    cat_str : str, optional
        Concatenate string between lines. Default: "\\n"

    Keyword Arguments
    -----------------

    Returns
    -------

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 10

        import os
        import plazy

        if __name__ == "__main__":
            path = '/home/plazy.txt'
            lines = [
                "hello",
                "world",
            ]
            plazy.write_txt(path=path, lines=lines)
            assert os.path.isfile(path)

    See Also
    --------
    read_txt
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

    Plazy version: 0.1.4+

    Parameters
    ----------
    path : str
        Path text file to read.
    line_func : callable, optional
        Function to process each line. Default: None
    skip_empty_line : bool, optional
        Skip empty line. Default: False

    Keyword Arguments
    -----------------

    Returns
    -------
    out : list
        List of lines

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 4,8,9,10,11,12

        import plazy

        if __name__ == "__main__":
            lines = plazy.read_txt(path='/home/video-list.txt')
            print(lines) # ['<line#1>', '<line#2>', '<line#3>', ...]

            # strip every text line, remove empty line in the list:
            lines = plazy.read_txt(
                path='/home/video-list.txt',
                line_func=lambda x : x.strip(),
                skip_empty_line=True
            )

    See Also
    --------
    write_txt
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
    """
    List files recursively in directory.

    Plazy version: 0.1.1+

    Parameters
    ----------
    root : str, optional
        Directory to traverse files. Default: "./" (current directory)
    filter_func : callable, optional
        Filter function to apply. Default: None
    is_include_root : bool, optional
        Include root directory path in the result. Default: False

    Keyword Arguments
    -----------------

    Returns
    -------
    out : list
        List of file paths

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 4,5,6

        import plazy

        if __name__ == "__main__":
            files = plazy.list_files(root='images',
                                    filter_func=lambda x : True if x.endswith('.jpg') else False,
                                    is_include_root=False)
            print(files) # ['1.jpg', '2.jpg', '_sub_/4.jpg']

    See Also
    --------
    """
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
