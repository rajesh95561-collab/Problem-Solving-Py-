# Recursive PowerSet Function in Python

# PowerSet: Given set S, return power set P(S) (all subsets of S).

# Input: String
# Output: Array of Strings (power set)

# Example: S = "123", P(S) = ['', '1', '2', '3', '12', '13', '23', '123']

def powerset1(xs):
    res = [[]]
    if len(xs) <= 0:
        return "Please Enter a parameter"
    if len(xs) == 1:
        res.append([xs[0]])
        return res
    else:
        z = []
        for i in powerset1(xs[1:]):
            z.append(i)
            z.append([xs[0]] + i)
        return z

final = powerset1('123')
print(final)
print(len(final))