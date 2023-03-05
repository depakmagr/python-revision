# Check whether a number is palindrome or not. Palindrome numbers are those which remain same even on reversing. Examples - 111, 131, 222, 212 etc.

    # input: 121 => The number is palindrome
    # input: 321 => The number is not palindrome

def is_palindrome(num):
    # Convert the number to a string and reverse it
    num_str = str(num)
    num_str_reversed = num_str[::-1]

    # Compare the original string with the reversed string
    if num_str == num_str_reversed:
        return True
    else:
        return False

# Test the function with some examples
print(is_palindrome(121))  # True
print(is_palindrome(321))  # False