# don't use lists/tuples/dictionaries as default parameters in function or class definitions:

def function(values=[]):
    values.append(1)
    return values

class Class:
    values = []

    def __init__(self):
        self.values.append(1)


if __name__ == '__main__':
    print(function())
    print(function())

    obj1 = Class()
    print(obj1.values)    
    obj2 = Class()
    print(obj1.values)
    
# $ python3 lists_as_default_param.py
# [1]
# [1, 1]
# [1]
# [1, 1]