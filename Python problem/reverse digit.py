# Write a program that reverses a four-digit number.
# Additionally, ensure that it checks whether the reversal is true.

number = int(input("Enter a number: "))
print(f"user input number is {number}")

a = number % 10
number = number // 10

b = number % 10
number = number // 10

c = number % 10
number = number // 10

d = number % 10

reverse = 1000*a + 100*b + 10*c + 1*d
print(f"Reverse number is {reverse}")