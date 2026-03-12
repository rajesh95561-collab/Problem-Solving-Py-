#1. Arbitrary Positional Arguments (*args)

# - Using *args lets you pass any number of positional arguments into a function.
# - Inside the function, they are collected into a tuple.

def flexi(*numbers):
    print(numbers)
    print(type(numbers))
    product = 1
    for i in numbers:
        product *= i
    return product

print(flexi(1,2,3))
print(flexi(1,2,3,4))
print(flexi(1,2,3,4,5))


# 2. Arbitrary Keyword Arguments (**kwargs)
# - Using **kwargs lets you pass any number of keyword arguments.
# - Inside the function, they are collected into a dictionary.

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Rajesh", age=21, city="Sambalpur")