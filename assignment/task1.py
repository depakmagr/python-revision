# # Write a python program that accepts an integer(n) and computes the value of n+nn+nnn+..........
#
# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n+1):
#     total += int(str(n)*i)
# print("The sum of n+nn+nnn+... is:", total)


n = int(input("Enter a number: "))
new_n = 0
summ = 0
for i in range(n):
    new_n = new_n * 10 + n   #=>" 0 * 10 + 5
    summ = summ + new_n
    print(new_n)

print("Total is : ", summ)