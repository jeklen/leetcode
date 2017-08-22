# mapping a list of functions
from math import sin, cos, tan, pi

def map_functions(x, functions):
    """map an iterable of functions on the object x"""
    res = []
    for func in functions:
        res.append(func(x))
    return res

family_of_funcions = (sin, cos, tan)
print(map_functions(pi, family_of_funcions))

# filter(function, sequence)
# filter out the elements that make the function returns True
fibonacii = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(filter(lambda x: x % 2, fibonacii))
print(odd_numbers)
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacii))
print(even_numbers)

## emamples of reduce()
# determining the maximum of a lsit of numerical value
from  functools import reduce
f = lambda a, b: a if (a>b) else b
r_reduce = reduce(f, [47, 11, 42, 102, 13])
print(r_reduce)