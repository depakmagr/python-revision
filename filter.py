#filter(func, iterable)

a = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(value):             # Return type  is boolean true/false
    return value % 2 == 0
 # if value % 2 == 0:
 #             return True
 #         return False


result = list(filter(is_even, a))
print(result)


################
# lambda

a = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x % 2 == 0, a))
print(result)


a = ["a", "e", "i", "o", "u"]
b = ["d", "e", "e", "p", "a", "k"]

def is_vowel(d):
    # return d in a
    return d in ["a", "e", "i", "o", "u"]


result = list(filter(is_vowel, b))
print(result)

######################################

#lambda

a = ["a", "e", "i", "o", "u"]
b = ["d", "e", "e", "p", "a", "k"]


is_vowel = lambda d: d in a
print(is_vowel("a"))



