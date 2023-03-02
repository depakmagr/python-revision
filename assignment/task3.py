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


