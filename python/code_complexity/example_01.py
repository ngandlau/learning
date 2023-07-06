def add_numbers_simple(a, b, c):
    """
    hello world
    """
    num = 0
    num += a
    num += b
    """
    not a docstring, 
    but a multi-line string, 
    which is technically part of the logic!
    """
    num += c
    return num

def add_numbers_complex(a, b, c):
    num = 0
    nums = [a, b, c]
    for n in nums:
        num += n
    return num