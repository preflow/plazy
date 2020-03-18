<img src='https://img.shields.io/pypi/l/plazy.svg'> <img src='https://codecov.io/gh/kyzas/plazy/branch/master/graph/badge.svg'> <img src='https://img.shields.io/pypi/pyversions/plazy.svg'> <img src='https://img.shields.io/pypi/v/plazy.svg'> <img src='https://img.shields.io/pypi/dm/plazy.svg'> <img src='https://img.shields.io/badge/code%20style-black-000000.svg'>

# plazy
Utilities for lazy Python developers

# INSTALLATION

```
pip install plazy
```

# PLAZY FEATURES

## Set object attributes from dictionary

Plazy version: 0.1.4+

Dynamically set object attributes from dictionary @ runtime

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

## Check whether string is a number

Plazy version: 0.1.4+

Check whether string is a number

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

## Unique list and string

Plazy version: 0.1.3+

Turn list or tuple into unique list/tuple, keep order or sort the list/tuple.

``` python
import plazy

if __name__ == "__main__":
    sample_t = (7, 3, 5, 3, 3, 7, 9)
    unique_t = plazy.unique(seq=sample_t) # (7, 3, 5, 9)

    sample_l = [7, 3, 5, 3, 3, 7, 9]
    unique_l = plazy.unique(seq=sample_l) # [7, 3, 5, 9]

    unique_rt = plazy.unique(seq=sample_t, sort=True, reverse=True) # (9, 7, 5, 3)
```

## Base64 encode and decode for string

Plazy version: 0.1.3+

Base64 encode and decode for string.

``` python
import plazy

if __name__ == "__main__":
    encoded_val = plazy.b64encode('plazy') # cGxhenk=
    encoded_val = plazy.b64encode('plazy', pretty=True) # cGxhenk => Note: this string cannot be decoded!
    original_val = plazy.b64decode('cGxhenk=') # plazy
```

## Random String

Plazy version: 0.1.2+

Generate random string.

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

## Read Text File

Plazy version: ~~0.1.2+~~, 0.1.4+

~~Read lines of text file, eliminate redundant characters of each line, skip the empty lines.~~

Read lines of text file as a list.

``` python
import plazy

if __name__ == "__main__":
    lines = plazy.read_txt(path='/home/video-list.txt')
    print(lines) # ['<line#1>', '<line#2>', '<line#3>', ...]

    # strip every text line, remove empty line in the list:
    lines = plazy.read_txt(path='/home/video-list.txt', line_func=lambda x : x.strip(), remove_empty=True)

    # -------------------------------
    # deprecated @ v0.1.2
    # lines = plazy.read_txt(path='/home/video-list.txt', strip=True)
    # print(lines) # ['<line#1>', '<line#2>', '<line#3>', ...]
    # lines = plazy.read_txt(path='/home/video-list.txt', strip=False) # no stripping
```

## Write Text File

Plazy version: 0.1.4+

Write text file.

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

## List Files

Plazy version: 0.1.1+

List files recursively in directory.

``` python
import plazy

if __name__ == "__main__":
    files = plazy.list_files(root='images',
                            filter_func=lambda x : True if x.endswith('.jpg') else False,
                            is_include_root=False)
    print(files) # ['1.jpg', '2.jpg', '_sub_/4.jpg']
```

## Auto Assign

Plazy version: 0.1.0+

Assign attributes of class with the passed arguments automatically.

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
