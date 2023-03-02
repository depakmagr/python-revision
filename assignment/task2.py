# write a python to calculate the difference beteween a given number and 17. If the number is greater than 17, return twice the absolute difference.

num = int(input("Enter a number: "))

if num >= 17:
    diff = (num - 17) * 2
    print("The difference between", num, "and 17 is", diff)
else:
    diff = (17 - num) * 2
    print("The difference between", num, "and 17 is", diff)