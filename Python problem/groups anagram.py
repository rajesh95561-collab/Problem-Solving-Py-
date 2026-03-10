
# Input: strs = ["act","pots","tops","cat","stop","hat"]
#
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

strs = ["act","pots","tops","cat","stop","hat"]
anagram = {}
for word in strs:
    sorted_word = "".join(sorted(word))
    if sorted_word not in anagram:
        anagram[sorted_word] = [word]
    else:
        anagram[sorted_word].append(word)
print(list(anagram.values()))