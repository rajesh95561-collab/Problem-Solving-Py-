class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os ,ram):
        print("Send the value to phone customer") 
        super().__init__(price,brand,camera) 
        # in Python, super().__init__(...) should always be the very first statement inside the child class constructor 
        #so that the parent class is initialized before any child-specific attributes are set
        self.os = os
        self.ram = ram
        print("inside Smartphone constructor")

s = SmartPhone(20000,"Nothing",12,"Android",2)
print(s.os)
print(s.brand)

# • 	In Python, you use  to call the parent constructor, which sets up base attributes before adding child-specific ones.
# • 	In C++, the same effect is achieved using an initializer list (), not .
# • 	For making objects callable: Python uses , while C++ requires overloading .
# • 	So,  in Python ≈ initializer list in C++, and  in Python ≈  in C++.
