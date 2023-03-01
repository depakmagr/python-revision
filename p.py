# Take three numbers as a user input and find the greatest among them.

a = int(input("Enter a first number"))
b = int(input("Enter a second number"))
c = int(input("Enter a third number"))
if a > b and a > c:
    print(f"{a} is greater")
elif b > c and b > c:
    print(f"{b} is largest")
else:
    print(f"{c} is greater")

