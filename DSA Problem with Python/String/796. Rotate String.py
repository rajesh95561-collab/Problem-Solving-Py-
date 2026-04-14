def method1(s,goal):
    if s == goal:
        return True
    else:
        for i in range(len(s)):
            match_str = s[i+1:]+s[0:i+1]
            if match_str == goal:
                return True
    return False

def method2(s,goal):
    if len(s) != len(goal):
        return False
    if goal in s + s:
        return True
    return False

s = "abcde"
goal = "cdeab"
print(method1(s,goal))
print(method2(s,goal))