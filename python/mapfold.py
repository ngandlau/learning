symbols = '$!§&%'

dummy = list(map(ord, symbols))
print(dummy)

dummy = list(filter(lambda x: x > 127, map(ord, symbols)))
print(dummy)
