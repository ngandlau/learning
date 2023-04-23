## Notes from "Fluent Python"

"Often _concrete strategies_ have no internal state [which would be implemented using class attributes]; they only deal with data from the _context_. If that is the case, then by all means **use plain old functions instead of coding single-method classes implementing a single-method interfaces declared in yet another class**. 

```python
# === Before: Strategy pattern with classes ===
class Order: # the context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Promotion] = None

class Promotion(ABC):
    @abstractmethod
    def discount(self, order: Order) -> Decimal: pass

class FidelityPromo(Promotion): ...
class BulkItemPromo(Promotion): ...
class LargeOrderPromo(Promotion): ...

# === After: Strategy pattern with functions ===
@dataclass(frozen=True)
class Order: # the context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None
    ...

def fidelity_promo(order: Order) -> Decimal: ...
def bulk_item_promo(order: Order) -> Decimal: ...
def large_order_promo(order: Order) -> Decimal: ...

```

---

"Once you get used to the ideqa that **functions are first-class objects**, it naturally follows that building data structures holding functions often makes sense (e.g. a list of functions, `List[Callable]`).

```python
# example
def fidelity_promo(order: Order) -> Decimal: ...
def bulk_item_promo(order: Order) -> Decimal: ...
def large_order_promo(order: Order) -> Decimal: ...

promos: List[Callable] = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order: Order) -> Decimal:
    return max(promo(order) for promo in promos)
```


## Persistent (remote) Terminal

```bash
tmux            # start terminal session, close with strg+bd
tmux detached
tmux attach     # restarts terminal session
```

## Returning same type

```python
from typing import TypeVar, Sequence

## Example 1 ***************************************************
# wrong typing
def do_nothing(x: Sequence) -> Sequence:
    return x

# correct typing
def do_nothing(x: SequenceT) -> SequenceT:
    return x

## Example 2 **************************************************
SequenceT = TypeVar('SequenceT', list, tuple, set)

def yyyymmdd(datetimes: SequenceT[datetime]) -> SequenceT[str]:
    result = [dt.strftime('%Y-%m-%d') for dt in datetimes]
    return type(datetimes)(result)
```

The typing is wrong. The function takes as argument a Sequence of datetimes and returns a Sequence of datetimes. This would hold if:

* Input: a _list_ of datetimes, Output: a _list_ of datetimes
* Input: a _list_ of datetimes, Output: a _tuple_ of datetimes (both _list_ and _tuple_ are of type Sequence, hence the type hints are not violated)

What we want to say is "if the input is a Sequence of type _list_, then we want to return a Sequence of the same type, namely type _list_". And so if the input sequence is of type _tuple_, we want to return a sequence of type _tuple_.

This can be achieved ... -> see fluent python

```python
from typing import TypeVar
from random import shuffle 
from collections.abc import Sequence, Hashable

T = TypeVar('T') # Generic TypeVar

def sample(population: Sequence[T], size: int) -> list[T]:
    result = shuffle(list(population))
    return result[:size]

# TypeVar T indicates that the type of the elements in the 
# returned list is the same as the type of the elements in
# the input sequence `population`
```

```python
# Generic TypeVar
T = TypeVar('T') 

# Restricted TypeVar
NumberT = TypeVar('NumberT', float, Decimal, Fraction) # Restricted TypeVar

# Bounded TypeVar
HashableT = TypeVar('HashableT', bound=Hashable)
# Hashable are objects of types like str, float, int, Decimal...
# Unhashable are objects of types like list, tuple, set, ...
```

## Debugging

```python
# import pdb

import code
code.interact(local=locals())

python -i script.py
```

## Better function design by minimizing dependencies

Before:

```python
class SimulationRun:
    name: str
    path_to_csv: str 

    def __init__(self, name):
        self.name = name
        self.path_to_csv = '/path/to/data/' + name + '.csv'

def calculate_things(simrun: SimulationRun):
    df = load(path=simrun.path_to_csv)
    # ...

```

*Problem*: If someone wants to copy the logic of `calculate_things()`, he needs also needs to copy the class `SimulationRun` because `calculate_things()` takes as argument an instance of `SimulationRun`. 

```python
# before: class SimulationRun is required to use calculate_things()
simrun = SimulationRun('name_of_simrun')
calculate_things(simrun=simrun)
```

But if we look at the implementation of `calculate_things()`, we find that the instance of `SimulationRun` is only used to get a path to a specific `.csv`-file.

It is better to get rid of the function's dependency on the `SimulationRun` class. We do that by changing the function such that it takes the path to the `.csv`-file directly:

```python
def calculate_things(path_to_csv: str):
    df = load(path=path_to_csv)
    # ...
```

With this implementation, we have the freedom to choose whether we want to use `SimulationRun` or not. We don't need `SimulationRun` if we know the path to the `.csv`-file:

```python
# after: with the help of SimulationRun
simrun = SimulationRun('name_of_simrun')
calculate_things(path_to_csv=simrun.path_to_csv)

# after: without the help of SimulationRun, which is no longer required
calculate_things(path_to_csv='path/to/data/name_of_simrun.csv')
```

## Composing SQL queries with psycopg2

```python
import psycopg2.sql as sql

cols = ['name', 'alter']

query = SQL("""
SELECT
    {select},
    COUNT(*)
FROM schema.table
WHERE 
    name LIKE 'Nils%'
    alter = 18
    {col1} = {val1}
    {col2} = {val2}
GROUP BY 
    {groupby}
""").format(
    select=sql.Identifier('name']),
    groupby=sql.SQL(', ').join([sql.Identifier(col) for col in cols])
    col1=sql.Identifier('alter'),
    val1=sql.Literal(18)
    # add filter 1=1 which doesn't filter anything
    col2=sql.Literal(1)
    val2=sql.Literal(1)
)

with get_connection(config) as conn:
    df = pd.read_sql(query, conn)
```

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
poetry install --extras "..." # install optional dependencies specified inside "..." 
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

## pydantic

Most useful for loading data from JSON files into Python. Pydantic allows you squish data from a JSON-file into the right format with specified datatypes.

* pydantic converts datatypes if possible. 
    * If the data is a string, but you want it to be float, it tries to convert to float: '29.99' -> 29.99
    * str -> bool: 't' -> True; 'f' -> False; '0' -> False, 'true' -> True

Example (from https://stefan.sofa-rockers.org/2020/05/29/attrs-dataclasses-pydantic/)

```console
>>> from datetime import datetime
>>> from pydantic import BaseModel
>>>
>>> class Child(BaseModel):
...     x: int
...     y: int
...     d: datetime
...
>>> class Parent(BaseModel):
...     name: str
...     child: Child
...
>>> data = {
...     'name': 'spam',
...     'child': {
...         'x': 23,
...         'y': '42',  # sic!
...         'd': '2020-05-04T13:37:00',
...     },
... }
>>> Parent(**data)
Parent(name='spam', child=Child(x=23, y=42, d=datetime.datetime(2020, 5, 4, 13, 37)))
```

## Test-Driven Development

[Interview with Martin Fowler](https://www.artima.com/articles/test-driven-development)

> If I'm creating a Money class, I'll make plus work first before I even think about the interface of multiply. Just get plus to work. Don't think about anything else, just focus on plus.

Don't plan the whole interface. Implement one method of the class, and do it in a way so that you can confidently claim: "this method works. It does exactly what it should do."

After the method does what it should it, *refactor* it to make it nice.

> I made it work, then I abstracted it.

So the process comes down to:

1. *develop*: work on a single method/function
2. *test*: write tests to check whether the function works as it should do
3. *refactor*: if you're tested the function, you can refactor it

Note that if you swap (1) with (2), you'll get *test-driven development*.

> It reduces the scope of what you have to think about. You don't have to think about everything you have to do in the class. You just have to think about one little piece of responsibility. You make that work and then you refactor it so everything is very nicely designed.
