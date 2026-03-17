# Write a program to swap the key-value pairs for the maximum and minimum values.
# For example, if the dictionary is like this {‘a’: 1, ‘b’: 2, ‘c’: 3}:
# The output should be {a: 3, b: 2, c: 1}.

D = {'a': 100, 'b': 200, 'c': 300, 'd': 400}

max_val = max(D.values())
min_val = min(D.values())
def max_key(D,max_val):
    for i in D:
        if D[i] == max_val:
            print("Maximum value:", D[i])
            return i
def min_key(D,min_val):
    for j in D:
        if D[j] == min_val:
            print("Minimum value:", D[j])
            return j

D[max_key(D,max_val)] = min_val
D[min_key(D,min_val)] = max_val

print("Updated Dictionary:", D)