# Input: s = "barfoothefoobarman", words = ["foo","bar"]
#
# Output: [0,9]
#
# Explanation:
#
# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
#
import itertools
s = "barfoothefoobarman"
words = ["foo","bar"]
check_list = []
res_list = []
for letter in itertools.permutations(words):
    check_list.append("".join(letter))
print(check_list)

for i in check_list:
    res_list.append(s.find(i))
print(res_list)


