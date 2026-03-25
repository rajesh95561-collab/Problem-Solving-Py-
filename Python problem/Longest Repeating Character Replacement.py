import collections

def replace(s, k):
    temp = []  # sliding window list
    left = 0  # pointer to shrink window
    max_len = 0  # track longest valid window

    for right in range(len(s)):
        temp.append(s[right])
        demo_dict = collections.Counter(temp)
        max_freq = max(demo_dict.values())

        # shrink window if replacements exceed k
        while len(temp) - max_freq > k:
            temp.pop(0)  # remove from front
            left += 1
            demo_dict = collections.Counter(temp)
            max_freq = max(demo_dict.values())

        max_len = max(max_len, len(temp))

    return max_len


# Example
s = "AABABCCBCCB"
k = 2
print(replace(s, k))  # Output: 6