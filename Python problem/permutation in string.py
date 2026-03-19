from collections import Counter

s1 = "abc"
s2 = "lecaabee"

len_s1 = len(s1)
count_s1 = Counter(s1)

found = False
for i in range(len(s2) - len_s1 + 1):
    window = s2[i:i+len_s1]
    if Counter(window) == count_s1:
        found = True
        break

print(found)