# -*- coding: utf-8 -*-
from . import data

from .coding import (
    auto_assign,
    auto_assign_strict,
    cloneable,
    random_string,
    setattr_from_dict
)

from .file import (
    list_files,
    read_txt,
    write_txt,
)

from .data import (
    b64encode,
    b64decode,
    unique,
    is_number,
    dt2ts,
    ts2dt,
)

from .singleton import (
    Singleton,
)

from .timer import (
    tic,
    toc,
    tictoc,
    get_tictoc,
)

__version__ = "0.1.6"
__all__ = [
    "auto_assign",
    "auto_assign_strict",
    "tic",
    "toc",
    "cloneable",
    "list_files",
    "read_txt",
    "write_txt",
    "random_string",
    "b64encode",
    "b64decode",
    "unique",
    "is_number",
    "dt2ts",
    "ts2dt",
    "setattr_from_dict",
    "Singleton",
    # TIMER
    "tic",
    "toc",
    "tictoc",
    "get_tictoc"
]
