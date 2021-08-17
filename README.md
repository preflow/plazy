<img src='https://img.shields.io/pypi/l/plazy.svg'> <img src='https://codecov.io/gh/kyzas/plazy/branch/master/graph/badge.svg'> <img src='https://img.shields.io/pypi/pyversions/plazy.svg'> <img src='https://img.shields.io/pypi/v/plazy.svg'> <img src='https://img.shields.io/pypi/dm/plazy.svg'> <img src='https://img.shields.io/badge/code%20style-black-000000.svg'>

# plazy
Utilities for lazy Python developers

```
pip install plazy
```

# Index

- [Coding](#coding)
  - [plazy.random_string(size=6, digit=True, lower=True, upper=True)](#random_string)
  - [plazy.b64encode(value, pretty=False)](#b64encode)
  - [plazy.b64decode(value)](#b64decode)
  - [plazy.setattr_from_dict(obj, kv, override=True)](#setattr_from_dict)
  - [@plazy.auto_assign](#auto_assign)
- [Data](#data)
  - [plazy.is_number(s)](#is_number)
  - [plazy.unique(seq, sort=False, reverse=False)](#unique)
- [File](#file)
  - [plazy.read_txt(path, line_func=None, skip_empty_line=False)](#read_txt)
  - [plazy.write_txt(path, lines, mode="w", cat_str="\n")](#write_txt)
  - [plazy.list_files(root, filter_func=None, is_include_root=False)](#list_files)

# PLAZY FEATURES

## Coding

### random_string

Plazy version: 0.1.2+

Generate random string.

**plazy.random_string(**

- size: length of random string. Default: 6
- digit: random string may contains digits. Default: True
- lower: random string may contains lowercases. Default: True
- upper: random string may contains uppercases. Default: True

**)**

``` python
import plazy

if __name__ == "__main__":
    rstring = plazy.random_string() # iVr3FY
    rstring = plazy.random_string(upper=False) # mzvn7b
    rstring = plazy.random_string(size=8) # XqVDuu5R
    rstring = plazy.random_string(size=6, digit=True, lower=False, upper=False) # 763099
    rstring = plazy.random_string(size=6, digit=False, lower=True, upper=False) # djzcch
    rstring = plazy.random_string(size=6, digit=False, lower=False, upper=True) # BGBMQN
```

[:link: Back to Index](#index)

### b64encode

### b64decode

Plazy version: 0.1.3+

Base64 encode and decode for string.

**plazy.b64encode(**

- **value**: value to encode base64
- pretty: remove "=" character at the end after encoding. Default: False

**)**

**plazy.b64decode(**

- **value**: encoded base64 value to decode

**)**

``` python
import plazy

if __name__ == "__main__":
    encoded_val = plazy.b64encode('plazy') # cGxhenk=
    encoded_val = plazy.b64encode('plazy', pretty=True) # cGxhenk => Note: this string cannot be decoded!
    original_val = plazy.b64decode('cGxhenk=') # plazy
```

[:link: Back to Index](#index)

### setattr_from_dict

Plazy version: 0.1.4+

Dynamically set object attributes from dictionary at runtime

**plazy.setattr_from_dict(**

- **obj**: object
- **kv**: dictionary of new attributes. Eg: {"name": "Peter", "age": 14}
- override: override old attribute(s). Default: True

**)**

``` python
import plazy

# Our custom class
class Person(object):
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    p1 = Person(name="plazy") # init a Person object
    plazy.setattr_from_dict(obj=p1, kv={
        "name": "yzalp",
        "age": 28,
    })
    print(p1.name) # "yzalp"
    print(p1.age)  # 28

    # set "override" to False
    p2 = Person(name="plazy") # init a Person object
    plazy.setattr_from_dict(obj=p2,
                            override=False,
                            kv={
                                "name": "yzalp",
                                "age": 28,
                            })
    print(p1.name) # "plazy" <- no overriding the pre-existed attribute due to "override=False"
    print(p1.age)  # 28

```

[:link: Back to Index](#index)

### auto_assign

Plazy version: 0.1.0+

Assign attributes of class with the passed arguments automatically.

**@play.auto_assign**

``` python
import plazy

class Cat(object):
    @plazy.auto_assign
    def __init__(self, name, owner='Kyzas'):
        pass

if __name__ == "__main__":
    my_cat = Cat('Kittie')
    print(my_cat.name)      # Kittie
    print(my_cat.owner)     # Kyzas
```

[:link: Back to Index](#index)

## Data

### is_number

Plazy version: 0.1.4+

Check whether string is a number

**plazy.is_number(**

- **s**: string to check

**)**

``` python
import plazy

if __name__ == "__main__":
    is_number = plazy.is_number("1")         # True
    is_number = plazy.is_number("0.234")     # True
    is_number = plazy.is_number("-0.234")    # True
    is_number = plazy.is_number("1e3")       # True
    is_number = plazy.is_number("plazy")     # False
    is_number = plazy.is_number("1.23k9")    # False
    is_number = plazy.is_number("x.3253254") # False
```

[:link: Back to Index](#index)

### unique

Plazy version: 0.1.3+

Turn list or tuple into unique list/tuple, keep order or sort the list/tuple.

**plazy.unique(**

- **seq**: sequence to process. Eg: [1, 3, 1, 2], (2, 5, 5, 1, 2), ...
- sort: Sort result. Default: False
- reverse: Reverse result. Default: False

**)**

``` python
import plazy

if __name__ == "__main__":
    unique_t = plazy.unique(seq=(7, 3, 5, 3, 3, 7, 9)) # -> (7, 3, 5, 9)    
    unique_l = plazy.unique(seq=[7, 3, 5, 3, 3, 7, 9]) # -> [7, 3, 5, 9]
    unique_rt = plazy.unique(seq=(7, 3, 5, 3, 3, 7, 9), sort=True, reverse=True) # -> (9, 7, 5, 3)
```

[:link: Back to Index](#index)

## File

### read_txt

Plazy version: ~~0.1.2+~~, 0.1.4+

~~Read lines of text file, eliminate redundant characters of each line, skip the empty lines.~~

Read lines of text file as a list.

**plazy.read_txt(**

- **path**: path to text file
- line_func: function to process each line. Default: None
- skip_empty_line: skip empty line. Default: False

**)**

``` python
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

    # -------------------------------
    # deprecated @ Plazy v0.1.2
    # lines = plazy.read_txt(path='/home/video-list.txt', strip=True)
    # print(lines) # ['<line#1>', '<line#2>', '<line#3>', ...]
    # lines = plazy.read_txt(path='/home/video-list.txt', strip=False) # no stripping
```

[:link: Back to Index](#index)

### write_txt

Plazy version: 0.1.4+

Write text file.

**plazy.write_txt(**

- **path**: path to text file
- **lines**: lines to write
- mode: write mode. Default: "w"
- cat_str: concat string between lines. Default: "\n" (new line character)

**)**

``` python
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
```

[:link: Back to Index](#index)

### list_files

Plazy version: 0.1.1+

List files recursively in directory.

**plazy.list_files(**

- root: directory to traverse files. Default: "./" (current directory)
- filter_func: filter function to apply. Default: None
- is_include_root: include root directory path in the result. Default: False

**)**

``` python
import plazy

if __name__ == "__main__":
    files = plazy.list_files(root='images',
                            filter_func=lambda x : True if x.endswith('.jpg') else False,
                            is_include_root=False)
    print(files) # ['1.jpg', '2.jpg', '_sub_/4.jpg']
```

[:link: Back to Index](#index)

# CONTRIBUTING

* Step 1. Fork on **dev** branch.
* Step 2. Install **pre-commit** on the local dev environment.

```
pip install pre-commit
pre-commit install
```

* Step 3. Write test case(s) for the new feature or the bug.
* Step 4. Write code to pass the tests.
* Step 5. Make sure that the new code passes all the pre-commmit conditions.

```
pre-commit run -a
```

* Step 6. Create pull request.
