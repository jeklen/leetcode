# filter object ?
# the first way
mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# the second way
def filterfunc(x):
    return x % 3 == 0
mult3 = filter(filterfunc, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# use list comprehension
mult3 = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x % 3 == 0]

# there are more usage
# 1 Returning a function from another function
def transform(n):
    return lambda x: x + n

f = transform(3)
print(f(4))
