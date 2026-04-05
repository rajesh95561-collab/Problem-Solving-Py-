
strs = ["dog","racecar","car"]
strs = sorted(strs)
result = ""
first_string = strs[0]
last_string = strs[-1]
for i in range(len(first_string)):
    if first_string[i] == last_string[i]:
        result += first_string[i]
    else:
        break
print(result)