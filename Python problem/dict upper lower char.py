# Write a function that accepts a string and returns the number of uppercase characters and lowercase characters as a dictionary.

def upper_lower(s):
    D={"upper":0,"lower":0}
    for i in s:
        if i>="a" and i<="z":
            D["lower"]+=1
        elif i>="A" and i<="Z":
            D["upper"]+=1
        else:
            continue
    return D

count_dict = upper_lower("HiiH")
print(count_dict)