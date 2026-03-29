# Find the length of a given string without using the len() function.
def length(s):
    global count
    for char in s:
        count = count + 1
    return count
count= 0
input_str = input("Enter a string: ")
count = length(input_str)
print(count)
