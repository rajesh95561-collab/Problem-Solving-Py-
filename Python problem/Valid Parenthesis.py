a = "[[]]"
a_list = list(a)
pairs = {')':'(', ']':'[', '}':'{'}
count_list = []

for i in range(len(a_list)):
    if a_list[i] in pairs.values():   # opening bracket
        count_list.append(a_list[i])
    elif a_list[i] in pairs:          # closing bracket
        if count_list and count_list[-1] == pairs[a_list[i]]:
            count_list.pop()
        else:
            print("False")
            break
else:
    print("True" if not count_list else "False")
