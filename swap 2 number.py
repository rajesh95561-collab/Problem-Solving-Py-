# The user will input two numbers.
# Write a program to swap the numbers.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

#using third variable
print(f"Before swaping number is {number1} and it is {number2}.")
temp = number1
number1 = number2
number2 = temp
print(f"After swaping(using third variable) number is {number1} and it is {number2}.")

#don't use third variable (tuple unpacking)
number1 , number2 = number2 , number1
print(f"After swaping(tuple unpacking) number is {number1} and it is {number2}.")

#using exclusive or
number1 = number1 ^ number2
number2 = number1 ^ number2
number1 = number1 ^ number2
print(f"After swaping(using exclusive or) number is {number1} and it is {number2}.")