# WAP capitalize each word of 1st later in a string

sample = input("enter your sample string: ")
list1 = sample.split(" ")
l = []

for i in list1:
    print(i.capitalize())
    l.append(i.capitalize())
print(" ".join(l))


