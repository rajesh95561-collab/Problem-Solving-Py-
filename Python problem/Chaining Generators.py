#This program generates Fibonacci numbers up to a given limit,
# then computes the square of each number using a generator.
# Finally, it sums all squared Fibonacci values and prints the result.
# Efficient use of generators avoids extra memory overhead.

def fibonacci_series(num):
    x,y = 0,1
    for i in range(num):
        x,y = y,x+y
        yield x
def square(nums):
    for num in nums:
        yield num**2
print(sum(square(fibonacci_series(50))))