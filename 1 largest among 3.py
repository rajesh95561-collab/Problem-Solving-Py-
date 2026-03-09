# User will input (3 person age).
# Find the oldest one.

first = int(input("Enter the first person age: "))
second = int(input("Enter the second person age: "))
third = int(input("Enter the third person age: "))

if first > second and first > third:
    print(f"The oldest person is {first} years old.")
elif second > first and second > third:
    print(f"The oldest person is {second} years old.")
elif third > first and third > second:
    print(f"The oldest person is {third} years old.")
else:
    print("Two or more persons have the same oldest age.")

# An f-string (formatted string literal) in Python is a way to embed variables or expressions directly inside a string, making output cleaner and easier to read.
