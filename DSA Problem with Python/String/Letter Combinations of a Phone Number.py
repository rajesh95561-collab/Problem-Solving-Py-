given_data = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
digits = "233"
res = []
def backtrack(idx, comb):
    global res
    global digits
    global given_data
    if not digits:
        return []
    if len(digits) == len(comb):
        res.append(comb)
        return None
    for ch in given_data[digits[idx]]:
        backtrack(idx + 1, comb + ch)
    return res

backtrack(0, "")
print(res)