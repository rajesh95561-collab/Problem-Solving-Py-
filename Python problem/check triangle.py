# Write a program that takes user input for three angles and determines whether they can form a triangle or not.

angle1 = int(input("enter the first angle"))
angle2 = int(input("enter the second angle"))
angle3 = int(input("enter the third angle"))

if (angle1+angle2+angle3) == 180 and angle1 != 0 and angle2 != 0 and angle3 != 0:
    print("IT IS A TRIANGLE")
else:
    print("IT IS NOT A TRIANGLE")
