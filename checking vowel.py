# Write a Python program to test whether a passed letter is a vowel o[r not.

vowels = ['a', 'e', 'i', 'o', 'u']
x = input("Enter a alphabets = ")

if x.lower() in vowels:
    print(f"{x} is a vowel letter.")

else:
    print(f"{x} is not a vowel letter.")
