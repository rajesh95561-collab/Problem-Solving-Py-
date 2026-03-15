# Write a program that can convert an integer to a string without using str().

def to_string(num):
    digits = "0123456789"
    result_string = ""

    while num !=0:
        curr_digit = num % 10
        result_string += digits[curr_digit]
        num //= 10

    return result_string[::-1]

print(to_string(1342))

#This program converts an integer into its string representation without using Python’s built-in str() function. It works by repeatedly extracting digits with modulus
# (% 10), mapping them to characters using a digit lookup string, and appending them to the result. Since digits are processed from right to left, the final string is
# reversed to produce the correct order.
