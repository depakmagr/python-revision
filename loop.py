## for Loop

for i in range(10):  # It range from 0 to 9
    print(i)


for i in range(1, 10):  # It range from 1 to 10
    print(i)


Find the even number from the first 10 natural numbers.

for i in range(1, 10):
    if i % 2 == 0:
        print(i)



""" For the first 30 number as it is; if otherwise divisible by 3 print 'Fizz', if divisible by 5 print 'Buzz', if divisible by both 3 and 5 print 'fizzBuzz' """

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}FizzBuzz", end=" ")
        break

    elif i % 3 == 0:
        print(f"{i}Fizz", end=" ")

    elif i % 5 == 0:
        print(f"{i}Buzz", end=" ")

    else:
        print(i, end=" ")



#range description(start,stop,size)

list = [1,2,3,4,5,6]

for i in [list , 'now']:
    print(i)

for x in "hey":
    print(x)






## Loop in dictionary

d = {
    "name": "ASD"
    "age": 23
    "address": "nakkhu"
}

print(list(d.keys()))
print(d.values())

## Looping in the dictionary keys.
for key in d.keys():
    print(key)



# # #Looping in the dictionary values
for values in d.values():
     print(values)

for i in d:  # This is same as d.keys() but only in the loop
     print(i)


print(d.items())
a, b = 1, 2  # tuple unpacking

for key, value in d.items():
    print(key, values)



a = [1, 2, 3, 4]

for i in a:
    print(i)

print(list(enumerate(a)))  #1, 2, 3, 4


for index, value in enumerate(a, start=1):       # Its takes value as given
    print(index, value)


# While Loop

counter = 0
while counter < 5 :
    counter += 1
    print(counter)






