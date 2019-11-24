#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re
from setuptools import setup

with io.open("plazy/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

setup(version=version)
