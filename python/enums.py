from enum import Enum, IntEnum, auto


class Colors(Enum):
    BLUE = 0
    RED = 0
    GREEN = 2

class Nuts(Enum):
    MACADAMIA = auto()
    CASHEW = auto()
    PEANUT = auto()

class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2


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
    print(Colors.BLUE == Colors.RED)
    print(Colors.BLUE.value == Colors.RED.value)

    # Enumeration members (BLUE, RED, GREEN) are hashable, hence can be used
    # as keys in dictionaries
    apples = {}
    apples[Colors.RED] = 'red delicious'
    apples[Colors.GREEN] = 'granny smith'

