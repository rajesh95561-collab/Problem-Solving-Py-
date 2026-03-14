# Problem Statement:
# Start with 1 pair of rabbits.
# Each pair becomes fertile after 1 month.
# Every fertile pair produces 1 new pair per month.
#Rabbits never die.
#after 12 month how many rabbit pair

def rabbit(m):
    if m==0 or m==1:
        return 1
    else:
        return rabbit(m-1)+rabbit(m-2)
print(rabbit(12))

# Recursive Fibonacci is inefficient because it repeatedly recalculates the same values, leading to exponential growth in the number of function calls. For example,
# to compute fib(5), the program ends up computing fib(3) and fib(2) multiple times, creating a large recursion tree with overlapping subproblems.
# This results in a time complexity of O(2^n), which becomes very slow as n increases. In contrast, iterative methods or recursion with memoization avoid this
# duplication by storing previously computed results, reducing the complexity to O(n) or even O(\log n) with advanced techniques.
