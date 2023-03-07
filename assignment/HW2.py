# Write a Python program to create a dictionary from a string. Track the count of the letters from the string.

input_str = "broadway"      # output = {"b":1,"r":1,"o":1,"a":2, "d":1,"w":1,"y":1}

letter_count = {}

# Loop through each character in the input string
for char in input_str:
    # If the character is already in the dictionary, increment its count
    if char in letter_count:
        letter_count[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        letter_count[char] = 1

print(letter_count)


a = "broadway"
dict = dict()
def string_dic(x):
    for i in x:
        dict[i] = x.count(i)
    print(dict)


string_dic(a)


