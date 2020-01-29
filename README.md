<img src='https://img.shields.io/pypi/l/plazy.svg'> <img src='https://codecov.io/gh/kyzas/plazy/branch/master/graph/badge.svg'> <img src='https://img.shields.io/pypi/pyversions/plazy.svg'> <img src='https://img.shields.io/pypi/v/plazy.svg'> <img src='https://img.shields.io/pypi/dm/plazy.svg'> <img src='https://img.shields.io/badge/code%20style-black-000000.svg'>

# plazy
Utilities for lazy Python developers

# INSTALLATION

```
pip install plazy
```

# PLAZY FEATURES

## Random String

Plazy version: 0.1.2+

Generate random string.

``` python
import plazy

if __name__ == "__main__":
    rstring = plazy.random_string(upper=False) # mzvn7b
    rstring = plazy.random_string() # iVr3FY
    rstring = plazy.random_string(size=8) # XqVDuu5R
    rstring = plazy.random_string(size=6, digit=True, lower=False, upper=False) # 763099
    rstring = plazy.random_string(size=6, digit=False, lower=True, upper=False) # djzcch
    rstring = plazy.random_string(size=6, digit=False, lower=False, upper=True) # BGBMQN
```

## Read Text File

Plazy version: 0.1.2+

Read lines of text file, eliminate redundant characters of each line, skip the empty lines.

``` python
import plazy

if __name__ == "__main__":
    lines = plazy.read_txt(path='/home/video-list.txt')
    print(lines) # ['<line#1>', '<line#2>', '<line#3>', ...]
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
