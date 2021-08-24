# -*- coding: utf-8 -*-
from .coding import (
    auto_assign,
    random_string,
    setattr_from_dict,
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
)

__version__ = "0.1.4"
__all__ = [
    "auto_assign",
    "list_files",
    "read_txt",
    "write_txt",
    "random_string",
    "b64encode",
    "b64decode",
    "unique",
    "is_number",
    "setattr_from_dict",
]
