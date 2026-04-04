dict_roman = {'I': 1, 'V': 5, 'X': 10,
              'L': 50, 'C': 100,
              'D': 500, 'M': 1000}

s = "LVIII"
total = 0
prev = 0

for ch in reversed(s):   # process from right to left
    current = dict_roman[ch]
    print(current)
    if current < prev:
        total -= current
    else:
        total += current
    prev = current

print(total)  # Output: 58