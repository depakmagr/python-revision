from functools import reduce


# def deps(a, b):
#     return a + b


# a = [1, 2, 3, 4, 5]
# result = reduce(deps, a)
# print(result)


##################
#lambda
a = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, a)
print(result)
