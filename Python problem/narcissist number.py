# Write a program that will take user input of a (4-digit number) and check whether the number is a narcissist number or not.

number = int(input("Enter a number: "))
original = number

a = number % 10
number =  number // 10
b = number % 10
number = number // 10
c = number % 10
number = number // 10
d = number % 10

if original == (a**4)+(b**4)+(c**4)+(d**4):
    print("The number is a narcissist number")
else:
    print("The number is not a narcissist number")