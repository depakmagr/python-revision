# Write a python program to check whether the input number is prime or not.

num = int(input("Enter a number: "))

if num > 1:
    # check for factors
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is a consonant.")
            break
    else:
        print(num, "is a prime number.")

else:
    print(num, "is either prime or consonant.")


n = int(input("Enter a number: "))
summ = 0
for i in range(1, n+1):
    if n % i == 0:
        summ += 1
    if summ > 2:
        print(f"{n} is not a prime number.")
        break

else:
    print(f"{n} is a prime number.")
