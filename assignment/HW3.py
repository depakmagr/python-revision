# Write a Python programto combine two dictionaries by adding values for common keys.

d1 = {'a':100,'b':200,'c':300}
d2 = {'a':300,'b':200,'d':400}              # output = {'a':400,'b':400,'d':400,'c':300}

# Initialize an empty dictionary to hold the combined values
combined_dict = {}

# Loop through each key in d1 and add its value to combined_dict
for key in d1:
    combined_dict[key] = d1[key]

    # If the key is also in d2, add its value to the existing value in combined_dict
    if key in d2:
        combined_dict[key] += d2[key]

# Loop through each key in d2 that's not already in combined_dict and add its value
for key in d2:
    if key not in combined_dict:
        combined_dict[key] = d2[key]

# Print the resulting combined dictionary
print(combined_dict)