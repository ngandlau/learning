def add_numbers_simple(a, b, c):
    num = 0
    num += a
    num += b
    num += c
    return num

def add_numbers_complex(a, b, c):
    num = 0
    nums = [a, b, c]
    for n in nums:
        num += n
    return num