# Write a program that will determine whether the given number is divisible by 3 and 6.

number = int(input("Enter a number: "))

if number % 6 == 0:
    print(f"The {number} is divisible by both 3 and 6")
elif number % 3 == 0:
    print(f"The {number} is divisible by 3 only")
else:
    print(f"The {number} is not divisible by 3 or 6")