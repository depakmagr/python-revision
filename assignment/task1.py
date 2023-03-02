# Write a python program that accepts an integer(n) and computes the value of n+nn+nnn+..........

n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total += int(str(n)*i)
print("The sum of n+nn+nnn+... is:", total)
