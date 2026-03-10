# Write a program to calculate the Euclidean distance between two coordinates.

pt_x1 =int(input("enter x1:"))
pt_y1 =int(input("enter y1:"))
pt_x2 =int(input("enter x2:"))
pt_y2 =int(input("enter y2:"))

d=((pt_x2-pt_x1)**2+(pt_y2-pt_y1)**2)**0.5
print(f"the distance is: {d}")