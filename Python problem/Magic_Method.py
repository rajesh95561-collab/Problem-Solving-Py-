import math

class Fraction:
    """
    Fraction Project:
    This project defines a Fraction class with operator overloading for arithmetic,
    comparison, and numeric operations. It demonstrates Python magic methods such as
    __add__, __sub__, __mul__, __truediv__, __mod__, __eq__, __ne__, and more.
    The class outputs descriptive strings to show how each operation is evaluated.
    """
    # constructor
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # numeric magic methods
    def __trunc__(self):
        return str(f"trunc({self.numerator}/{self.denominator}) = {math.trunc(self.numerator/self.denominator)}")

    def __round__(self, n=0):
        return str(f"round({self.numerator}/{self.denominator}, {n}) = {round(self.numerator/self.denominator, n)}")

    def __abs__(self):
        return str(f"abs({self.numerator}/{self.denominator}) = {abs(self.numerator/self.denominator)}")

    def __neg__(self):
        return str(f"neg({self.numerator}/{self.denominator}) = {-self.numerator/self.denominator}")

    def __pos__(self):
        return str(f"pos({self.numerator}/{self.denominator}) = {+self.numerator/self.denominator}")

    # string magic methods
    def __str__(self):
        return str(f"{self.numerator}/{self.denominator} = {self.numerator/self.denominator}")

    def __repr__(self):
        return str(f"Fraction({self.numerator}, {self.denominator})")

    def __bool__(self):
        return str(f"bool({self.numerator}/{self.denominator}) = {self.numerator != 0}")

    # comparison magic methods
    def __eq__(self, other):
        return str(f"({self.numerator}/{self.denominator}) == ({other.numerator}/{other.denominator}) = {(self.numerator/self.denominator) == (other.numerator/other.denominator)}")

    def __ne__(self, other):
        return str(f"({self.numerator}/{self.denominator}) != ({other.numerator}/{other.denominator}) = {(self.numerator/self.denominator) != (other.numerator/other.denominator)}")

    def __lt__(self, other):
        return str(f"({self.numerator}/{self.denominator}) < ({other.numerator}/{other.denominator}) = {(self.numerator/self.denominator) < (other.numerator/other.denominator)}")

    def __gt__(self, other):
        return str(f"({self.numerator}/{self.denominator}) > ({other.numerator}/{other.denominator}) = {(self.numerator/self.denominator) > (other.numerator/other.denominator)}")

    def __ge__(self, other):
        return str(f"({self.numerator}/{self.denominator}) >= ({other.numerator}/{other.denominator}) = {(self.numerator/self.denominator) >= (other.numerator/other.denominator)}")

    # arithmetic magic methods
    def __add__(self, other):
        temp_num = self.numerator * other.denominator + other.numerator * self.denominator
        temp_den = self.denominator * other.denominator
        return str(f"({self.numerator}/{self.denominator}) + ({other.numerator}/{other.denominator}) = {temp_num}/{temp_den}")

    def __sub__(self, other):
        temp_num = self.numerator * other.denominator - other.numerator * self.denominator
        temp_den = self.denominator * other.denominator
        return str(f"({self.numerator}/{self.denominator}) - ({other.numerator}/{other.denominator}) = {temp_num}/{temp_den}")

    def __mul__(self, other):
        temp_num = self.numerator * other.numerator
        temp_den = self.denominator * other.denominator
        return str(f"({self.numerator}/{self.denominator}) * ({other.numerator}/{other.denominator}) = {temp_num}/{temp_den}")

    def __truediv__(self, other):
        temp_num = self.numerator * other.denominator
        temp_den = self.denominator * other.numerator
        return str(f"({self.numerator}/{self.denominator}) / ({other.numerator}/{other.denominator}) = {temp_num}/{temp_den}")

    def __mod__(self, other):
        val_self = self.numerator / self.denominator
        val_other = other.numerator / other.denominator
        return str(f"({self.numerator}/{self.denominator}) % ({other.numerator}/{other.denominator}) = {val_self % val_other}")


# usage
if __name__ == "__main__":  #separate reusable code from test/demo code.
    x = Fraction(1, 2)
    y = Fraction(3, 4)

    print(Fraction.__doc__)  #__doc__
    print(x)          # __str__
    print(repr(y))    # __repr__
    print(x + y)      # __add__
    print(x - y)      # __sub__
    print(x * y)      # __mul__
    print(x / y)      # __truediv__
    print(x % y)      # __mod__
    print(x == y)     # __eq__
    print(x != y)     # __ne__
    print(x < y)      # __lt__
    print(x > y)      # __gt__
    print(x >= y)     # __ge__
    print(x.__trunc__())  # __trunc__
    print(x.__round__(2)) # __round__
    print(x.__abs__())    # __abs__
    print(x.__neg__())    # __neg__
    print(x.__pos__())    # __pos__
    print(x.__bool__())   # __bool__