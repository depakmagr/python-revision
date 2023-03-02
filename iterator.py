# names = ['Gabs', 'Deeps']
# name = iter(names)
#
# print(next(name))
#
# print(next(name))
#
# print(next(name))


language = 'Deeps'
name = iter(language)

print(next(name))

print(next(name))

print(next(name))

print(next(name))

print(next(name))


# Write a program by using while loop with iteration

names = ['Gabs', 'Deeps']
w
name_iter = iter(names)

while True:
    try:
        name = next(name_iter)
        print(name)

    except StopIteration:
        break

