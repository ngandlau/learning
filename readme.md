## Interfaces in Python using `ABC` and `@abstractmethod`

```python
from abc import ABC, abstractmethod

class IDatabaseConnector(ABC):

    @abstractmethod
    def write(self):
        raise NotImplementedError
        
class PostgresConnector(IDatabaseConnector):

    def write(self):
        pass

class MysqlConnector(IDatabaseConnector):
    pass


if __name__ == '__main__':
    # instantiation works, b/c all abstract methods implemented
    postgres = PostgresConnector() 

    # instantiation throws error, b/c not all abstract methods implemented 
    mysql = MysqlConnector()  
```

## git command

```console
foo@bar:~$ git reset --hard HEAD
foo@bar:~$ git reset --hard HEAD~1
```

## enums

An enumeration is a set of symbolic names bound to unique, constant values. 

```python
from enum import Enum


class Colors(Enum):
    BLUE = 0
    RED = 0
    GREEN = 2

if __name__ == '__main__':
    print(repr(Colors.BLUE))
    print(Colors.BLUE)
    print(Colors.BLUE.value)
    print(Colors.BLUE.name)

    print()
    for color in Colors:
        print(color)

    # Because BLUE=0 and RED=0, it's like BLUE and RED are the same!
    print()
    print(len(Colors))
    print(color.BLUE == color.RED)
    print(color.BLUE.value == color.RED.value)

    # Enumeration members (BLUE, RED, GREEN) are hashable, hence can be used
    # as keys in dictionaries
    apples = {}
    apples[Colors.RED] = 'red delicious'
    apples[Colors.GREEN] = 'granny smith'
```

Running the script:

```console
foo@bar:~$ python enums.py

<Colors.BLUE: 0>
Colors.BLUE
0
BLUE

Colors.BLUE
Colors.GREEN

2
True
True
```
	
## virtualenv in python

virtuelenv is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally (usually done with `pip install <package>`) which could break system tools or other projects.

You setup a virtualenv for every new project (think: repo) that you start. If you then activate the venv, any package that you install via `pip install <package>` will be installed in that specific virtual environment, and not globally.

You create a virtual environment in your project's directory. This creates a new directory `/path/to/project/env` that contains all the stuff of the virtual environment.

```console
foo@bar:~$ python3 -m venv env
```

Whenever you're working on your project, **activate** the environment:

```console
foo@bar:~$ source env/bin/activate
```

When you're done, **deactivate** the environment:

```console
foo@bar:~$ deactivate
```

## managing different python installations

If you have multiple python installations running, there exist some naming conventions. For example, `usr/bin/python2` is reserved for your installation of Python2.7, and `/usr/bin/python3` is reserved for your installation of Python3.x.

```console
foo@bar:~$ which python
/usr/bin/python

foo@bar:~$ which python2
/usr/bin/python2

foo@bar:~$ which python3
/usr/bin/python3
```

## Git workflow

New commands:

```console
git log
git log --graph
git stash
git stash pop
git rebase -i master
git commit -a --amend
git reset --hard HEAD~
git rebase --abort
git rebase -i master
git rebase continue
git push -f
git push -f origin <branch_name>
git branch -D <branch_name>
```

## pathlib, Path 

`Path` extends a string containing a path with additional functionality.

```python
from pathlib import Path

Path.cwd()
Path.home()


my_path = Path('/home/user/')

my_path.iterdir()
my_path.absolute()
my_path.mkdir()
```

## logging

If you want to report events that occur during the normal operation of a program (e.g. for status monitoring or fault investigation), you use *logs*.

* **warnings**: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
* **info**: Confirmation that things are working as expected; for very detailed output for diagnostic purposes.

```python 
# logger.py
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

logger = logging.getLogger(__name__)

logger.warning('some warning')
logger.info('some info')
```

```console
$ python logger.py
07/20/2022 06:48:56 PM Hello warning
07/20/2022 06:48:56 PM Goodbye info
```

## psycopg2

```python
config = {
    'host'      : '',
    'port'      : '',
    'dbname'    : '',
    'user'      : '',
    'password'  : '',
}

conn = psycopg2.connect(config)

with conn:
    with conn.cursor() as curs:
        curs.execute(SQL1)

with conn:
    with conn.cursor() as curs:
        curs.execute(SQL2)

conn.close()

```

## workflow with poetry

```console
git clone <repo_name>
poetry install              # creates a venv, installs all non-optional (!) dependencies
poetry install --exit "..." # install optional dependencies specified inside "..." 
poetry shell                # activates venv
deactivate                  # deactivate venv
```

## environment variables

Environment variables are variables in *your* system that describe *your* environment.

PATH is an environment variable that contains the paths to all folders that might contain executables. Your machine will look for executables in the directories specified in PATH. So when you run `~$ python` in your terminal, your machine looks for Python's executable in the directories listed in PATH. 

You can always run executables in your terminal by specifying the absolute path, but that would be tedious. For example, we could run python on our machine by saying 

```console
~$ /usr/bin/python
```

which is much more complicated than just saying 

```console
~$ python
```

---

You can also define your own environment variables. It is useful to set environment variables like `GOOGLE_ACCOUNT_USERNAME` and `GOOGLE_ACCOUNT_PASSWORD`.

To set an environment variable in Linux, add a line in your `.bashrc` file:

```
export GOOGLE_ACCOUNT_USERNAME=myusername
export GOOGLE_ACCOUNT_PASSWORD=mypassword
```

Once these environment variables are set, you can consume them in python:

```python
import os

google_username = os.environ['GOOGLE_ACCOUNT_USERNAME']
google_password = os.environ['GOOGLE_ACCOUNT_PASSWORD']
```

## copy-on-write

Suppose you have a dataframe `df_1` and you want to make a copy `df_2` on which you want to make modifications. The idea of [Copy-on-write](https://en.wikipedia.org/wiki/Copy-on-write) is that not until you made any modification on `df_2`, there is no need to make the copy. For as long as `df_1` and `df_2` are the same, they can share the same resource. A new resource must only be created once you modify `df_2`.

## shallow copy vs deep copy

A deep copy is what non-programmers assume a copy is: a copy of an object that is completely independent from the original object. If I copy an artwork, the copy is completely independent of the original. If one removes paint from the original, my copy remains unaffected.

In programming, a deep copy of a collection object (eg, a list or dataframe) is completely independent of the original object. The copy constructs a *new* collection object and recursively populates it with *copies* of the child objects (the elements of the list, or the data in the dataframe). Thus, if I change an element of the copy, the elements of the original remain unchanged.

A *shallow copy* constructs a *new* collection object, but does not copy the child objects. Instead, the new collection object is populated with *references* to the child objects of the original object. That leads to the following behavior:

* appending a new element to `copy` will not affect `original`. The new element is in `copy` but not in `original`
* changing an element in `copy` will change the same element in `original`, because the elements of `copy` point to the elements of `original`.

For illustrative examples, look at this [Jupyter Notebook](https://github.com/ngandlau/learning/blob/master/python/deep_vs_shallow_copy.ipynb).


