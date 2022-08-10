# Print the sum, difference and product of two complex numbers by creating a class named 'Complex' with separate
# methods for each operation whose real and imaginary parts are entered by the user.
class Complex():
    def __init__(self):
        self.imgPart = None
        self.realPart = None

    def initComplex(self):
        self.realPart = int(input("Enter the Real Part:"))
        self.imgPart = int(input("Enter the ImaginaryPart: "))

    def display(self):
        print(self.realPart, "+", self.imgPart, "i", sep="")

    def sum(self, c1, c2):
        self.realPart = c1.realPart + c2.realPart
        self.imgPart = c1.imgPart + c2.imgPart

    def difference(self, c1, c2):
        self.realPart = c1.realPart - c2.realPart
        self.imgPart = c1.imgPart - c2.imgPart

    def product(self, c1, c2):
        self.realPart = c1.realPart * c2.realPart
        self.imgPart = c1.imgPart * c2.imgPart


c1 = Complex()
c2 = Complex()
c3 = Complex()
c4 = Complex()
c5 = Complex()
print("Enter first complex number")
c1.initComplex()
print("First Complex Number: ", end="")
c1.display()
print("Enter second complex number")
c2.initComplex()
print("Second Complex Number: ", end="")
c2.display()
print("Sum of two complex numbers is ", end="")
c3.sum(c1, c2)
c3.display()
print("Difference of two complex numbers is ", end="")
c4.difference(c1, c2)
c4.display()
print("Product of two complex numbers is ", end="")
c5.product(c1, c2)
c5.display()

#output
"""
Enter first complex number
Enter the Real Part:4
Enter the ImaginaryPart: 5
First Complex Number: 4+5i
Enter second complex number
Enter the Real Part:2
Enter the ImaginaryPart: 1
Second Complex Number: 2+1i
Sum of two complex numbers is 6+6i
Difference of two complex numbers is 2+4i
Product of two complex numbers is 8+5i
"""
# 2. Create an abstract class representing equilateral polygon with required
# abstract and concrete methods and properties to calculate area and perimeter
# of it. Create classes for Rectangle, Square and Regular Pentagon by
# implementing a polygon class to calculate the area and perimeter of them.
# Also overload the comparison operators for above classes to compare them by
# their calculated area.
# In the main function, ask the user number of sides and length of the polygon
# and print their area and perimeter accordingly
from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    def area(self):
        pass


class Rectangle(Polygon):
    def perimeter(self, length, breadth):
        return 2 * (length + breadth)

    def area(self, length, breadth):
        return length * breadth


class Square(Polygon):
    def perimeter(self, length, sides):
        return sides * length

    def area(self, length):
        return length * length


class Rpentagon(Polygon):
    def perimeter(self, length, sides):
        return sides * length

    def area(self, length, sides):
        return 1 / 2 * sides * length * length


length = int(input("Enter length of polygon "))
breadth = int(input("Enter breadth of polygon "))
sidesR = int(input("Enter sides of rectangle "))
sidesS = int(input("Enter sides of square "))
sidesP = int(input("Enter sides of pentagon "))
R = Rectangle()
print("Perimeter and Area of Rectangle are ")
print(R.perimeter(length, breadth), R.area(length, breadth))
S = Square()
print("Perimeter and Area of square are ")
print(S.perimeter(length, sidesS), S.area(length))
P = Rpentagon()
print("Perimeter and Area of regular pentagon are ")
print(P.perimeter(length, sidesP), P.area(length, sidesP))

#output

