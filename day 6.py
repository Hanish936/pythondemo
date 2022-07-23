"""
...........Inheritence........
the
process
of
creating
a
new


class by using the properties of same class.


EXAMPLE....


class A:
    def f1(self)

        print('A')


class B(A):
    def f2(self)

        print('B')


ob = B()
ob.f1()
ob.f2()

TYPES::
SINGLE
INHERITENCE:


class A: //

    / its
a
parent


class or super class


def f1(self)
    print('A')


class B(A): //

    / its
a
child


class
    def f2(self)

        print('B')


ob = B()
ob.f1()
ob.f2()

MULTILEVEL
INHERITENCE:: more
thn
one
classes.


class A():
    def f1():

        print('A')


class B('A'):
    def f2(self):

        print('B')


class C(B):
    def f3(self):

        print('C')


ob = c()
ob.f1()
ob.f2
ob.f3

MULTIPLE
INHERITENCE:: same as upper

hierrarchical::

class A():
    def f1():

        print('A')


class B('A'):
    def f2(self):

        print('B')


class C(B):
    def f3(self):

        print('C')


ob = c()
ob.f1()
ob.f3()

ehdech
f2
nhi
hoyega
execute.

HYBRID
INHERITENCE:
multiple + herirarchal ??


SUPER
KEYWORD: is used
to
access
variables
of
parent


class in child class.


class A()
    a = 10


b = 20


def _init_(self)
"""
"""
...........Inheritence........
the
process
of
creating
a
new


class by using the properties of same class.


EXAMPLE....


class A:
    def f1(self)

        print('A')


class B(A):
    def f2(self)

        print('B')


ob = B()
ob.f1()
ob.f2()

TYPES::
SINGLE
INHERITENCE:


class A: //

    / its
a
parent


class or super class


def f1(self)
    print('A')


class B(A): //

    / its
a
child


class
    def f2(self)

        print('B')


ob = B()
ob.f1()
ob.f2()

MULTILEVEL
INHERITENCE:: more
thn
one
classes.


class A():
    def f1():

        print('A')


class B('A'):
    def f2(self):

        print('B')


class C(B):
    def f3(self):

        print('C')


ob = c()
ob.f1()
ob.f2
ob.f3

MULTIPLE
INHERITENCE:: same as upper

hierrarchical::

class A():
    def f1():

        print('A')


class B('A'):
    def f2(self):

        print('B')


class C(B):
    def f3(self):

        print('C')


ob = c()
ob.f1()
ob.f3()

ehdech
f2
nhi
hoyega
execute.

HYBRID
INHERITENCE:
multiple + herirarchal ??


SUPER
KEYWORD: is used
to
access
variables
of
parent


class in child class.


class A()
    a = 10


b = 20


def _init_(self)
    print('A')


def m1(self):
    print('m1')


classB(A)


def display()


.................example.............


class A()
    def _init_(self)
        print('A')

    def m1(self):
        print('m1')


classB(A)
a = 4
b = 5

def m2 9
self):
print(self.a, self.b)
print(super(), super().b)
ob = b()
ob.m1()
ob.m2()
    .....example........
class A()
    a = 10
b = 20
def _init_(self)
    print('A')
def m1(self):
    print('m1')
classB(A)

a = 4
b = 5


def m2(self):
    super().m1()


print(self.a, self.b)
print(super(), super().b)
ob = b()
ob.m1()
ob.m2()

.......EXample......


class A()
    a = 10


b = 20


def _init_(self)
    print('A')


def m1(self):
    print('m1')


classB(A)

a = 4
b = 5

def_init_(self)
super()._init_(12, 12)


def m2(self):
    super().m1()
    print(self.a, self.b)
    print(super(), super().b)


ob = b()
ob.m1()
ob.m2()

POLYMORPHISM::

1.
COMPILE
TIME:: OVERLOADING
2.
RUN
TIME:: OVERRIDING
OPERATOR
CONSTRUCTOR
FUNCTION

Python
doesnt
support
overloading.Python
does
supports
overriding.

......example
1.....compile
time.....

classA()


def f1(self.


    A, B)
print('A')


def f1(self.


    A, B, C)


..........example
2......run
time......


class A()
    a = 10


b = 20


def _init_(self)
    print('a')


def m1(self):
    print('m1')


classB(A)

a = 4
b = 5


def m1(self):
    print('B class')


ob = b()
ob.m1()
'''
MODULES::
just
like
header
files in c + +..we
use
modules in python.
1.
PRE
DEFINED:: Eg: DATE, TIME
.......EXAMPE......
'''
from math import *
import math as m
import math

.m.sqrt()
sqrt()
#2.
#USER
#DEFINED::
"""

# single inheritance

# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class


class Child(Parent):
	def func2(self):
		print("This function is in child class.")


object = Child()
object.func1()
object.func2()


# multiple inheritance

class Mother:
	mothername = ""

	def mother(self):
		print(self.mothername)

class Father:
	fathername = ""

	def father(self):
		print(self.fathername)


class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)


s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

# multilevel inheritance

class Grandfather:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername

		Grandfather.__init__(self, grandfathername)

class Son(Father):
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname
m
		Father.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)


s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

# Hierarchical inheritance

class Parent:
	def func1(self):
		print("This function is in parent class.")
class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")

class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")


object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

# hybrid inheritance

class School:
	def func1(self):
		print("This function is in school.")
class Student1(School):
	def func2(self):
		print("This function is in student 1. ")
class Student2(School):
	def func3(self):
		print("This function is in student 2.")
class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")
object = Student3()
object.func1()
object.func2()

#polymorphism

class Bird:
    def intro(self):
        print("There are different types of birds")

    def flight(self):
        print("Most of the birds can fly but some cannot")


class parrot(Bird):
    def flight(self):
        print("Parrots can fly")


class penguin(Bird):
    def flight(self):
        print("Penguins do not fly")

obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()

obj_bird.intro()
obj_bird.flight()

obj_parr.intro()
obj_parr.flight()

obj_peng.intro()
obj_peng.flight()


#modules
from math import sqrt, factorial

print(sqrt(16))
print(factorial(6))



