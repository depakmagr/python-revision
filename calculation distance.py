## Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

fun = (x2 - x1) ** 2 + (y2 - y1) ** 2 ** 1/2
print("Distance is ", fun)


d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance is ", d)