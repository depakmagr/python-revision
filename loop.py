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