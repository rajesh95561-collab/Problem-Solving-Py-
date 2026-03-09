# Write a program that will give you the sum of three digits.

number = int(input("Enter a number: "))
a = number % 10
number = number // 10
b = number % 10
number = number // 10
c = number % 10
number = number // 10
# // Returns the integer quotient (rounded down to the nearest whole number).


print(a+b+c)