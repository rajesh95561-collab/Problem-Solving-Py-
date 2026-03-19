# Program Documentation
# This program defines a Customer class with attributes for name and gender. A separate greet function takes a Customer object and prints a personalized greeting
# based on gender. The logic uses case-insensitive comparison to ensure consistent results. It demonstrates Python’s object-oriented design and pass-by-reference
# behavior when passing class instances to functions.

class Customer:
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender

def greet(customer):
    print(id(customer))  #memory add - 1790055435296(customer is the ref of the cust)
    customer._name = customer._name.upper()
    if customer._gender.lower() == "male":
        print(f"Hii {customer._name} sir")
    else:
        print(f"Hii {customer._name} ma'am")

cust = Customer("Rajeswari", "female")
print(id(cust))   #1790055435296
greet(cust)
