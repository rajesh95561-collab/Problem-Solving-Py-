# multiplication don't  use * operator
# using loop

def mult(a,b):
    result = 0
    for i in range(b):
        result += a
    print(result)

mult(5,3)

# using recursion
def mult_recursive(a,b):
    if b == 0:
        return 0
    else:
        return a + mult_recursive(a,b-1)

print(mult_recursive(2,3))