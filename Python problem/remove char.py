# Write a program that can remove a particular character from a string.

str1 = input("Enter a string ")
remove_char = input("Enter a char you want to remove ")

temp_list = list(str1)
if remove_char in temp_list:
    temp_list.remove(remove_char)
for i in temp_list:
    str1 = "".join(temp_list)

print(str1)
