# Write a program that can calculate the factorial of a given number provided by the user.

number = int(input("Enter a number: "))

def factorial(facto):
    if facto == 0:
        return 1
    else:
        return facto * factorial(facto - 1)

fact = factorial(number)
print(f"the factorial of {number} is {fact}")