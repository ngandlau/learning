from typing import TypeVar


SequenceT = TypeVar('SequenceT', list, tuple, set)

# no issues found by mypy
def do_nothing(x: SequenceT) -> SequenceT:
    return x

# issues found by mypy
def do_nothing_err(x: SequenceT) -> SequenceT:
    return list(x)
    
