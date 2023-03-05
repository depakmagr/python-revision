b = ["d", "e", "e", "p", "a", "k"]


def capitalize(value):
    return value.upper()


result = list(map(lambda x: x.upper, b))
print(result("c"))



###########
# this is the reason checker.
# if 'V':
#     print("Here")
# bool("V")