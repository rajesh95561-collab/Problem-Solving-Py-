haystack = "adbutsad"
needle = "bad"

#method 1
if needle in haystack:
    print(haystack.index(needle))
else:
    print(-1)

#method 2
n, m = len(haystack), len(needle)
for i in range(n - m + 1):
    if haystack[i:i + m] == needle:
        print(i)

#method 3
print(haystack.find(needle))