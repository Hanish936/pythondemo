'''
ENCAPSULATIONS
AND
ABSTRACTION::


Process
of
binding
a
data is called
ENCAPSULATION.
TWO
keyword:
1.
Protected::                _ < variable
name > // protected


class A
    def _init_(self):
        self._a = 14


classB(A):


def _init_(self):
    A._init_(self)
    print(self._a)


2.
Private::  (double underscore)
__ < variable
name >.// outside
the


class we cannot use the private keyword.


__a = 10 // private


def __sum(self):
    print(self.__a)


def display self

):
print('A')
ob = A()
ob.__sum()
ob = A()
ob.display()

    .....getter
setter
classes
are
used
when
multiple
data is there.we
declare
aprivate
variable..........


class A:
    __song
    name = " "

    def setSongName(song name

    ):
    self.__song
    name = song
    name


def get SongName()


return self.__song
name

ob = A()
ob.setSongName("  ")
print(ob.get
Song
Name())



..............ABSTRACTION................
Data
hiding.eg
ATM
machine.
cannot
creat
object in abstract


class than in normal class.


from abc import ABC, abstract

method


class student(ABC)  // dont define the function.no body just use the pass statement.


@abstract


method // keyword... // decorator..


def m1(self):
    pass


class A(student):
    def m1(self):
        print('hello')


ob = A
ob.m1()

..........EXCEPTION..........
DISTURB
THE
NORMAL
FLOW
OF
PROGRAM..

............KEYWORDS
IN
EXCEPTION
HANDLING...............
1.
try
    2.except
    3. else
    4.
    raise::if we want to raise the exception itself..
    5.finally



    we
    can
    give
    the
    name
    of
    the
    error
    following
    the
    keywords.

    # we cannont cancatinate int with string..

    example............
    try
        a = "10"
    print(a + "hello").
    .
    .
    .
    .
    .
    .
    .
    .

    example
    of
    raise::

    class Invalid Number(base exception)


    def _init_(self.


        str)
    super()._init_(self):
    self.str = str
'''

# try exception handling
print('H')
# print(10/0)   //show error in code thats why we write it in try block
try:
    a = 10
    print(a / 0)
except ZeroDivisionError as z:  # (ZeroDivisionError,TypeError) #used as multiple error types
    print('z')
else:
    print('Hello')
print('Z')


# try except else
def AbyB(d, b):
    try:
        c = ((d + b) / (d - b))
    except ZeroDivisionError:
        print("a/b result in 0")

    else:
        print(c)


# raise
try:
    x = int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")


# Encapsulation
# private
class Base:
    def ABX(self):
        self.a = "2"
        self.__c = "3"


# Creating a derived class
class Derived(Base):
    def _init_(self):
        # Calling constructor of
        # Base class
        Base.ABX(self)
        print("Calling private member of base class: ")
        print(self.__c)


obj1 = Base()
print(obj1.a)


# protected
class Base:
    def _init_(self):
        # Protected member
        self._a = 2


# Creating a derived class
class honey(Base):
    def _init_(self):
        # Calling constructor of
        # Base class
        Base._init_(self)
        print("Calling protected member of base class: ",
              self._a)

        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)


obj1 = honey()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)

# Abstraction
# example 1
from abc import ABC, abstractmethod


class student(ABC):
    @abstractmethod  # it is called as decorator
    def m1(self):
        pass  # we just declare it instead of defining body here


class A(student):
    def m1(self):
        print('Hello')


ob = A()
ob.m1()


# get setter function
class hanish:
    def __init__(self):
        self._age = None

    def _init_(self, age=0):
        self._age = age
        # using the getter method

    def get_age(self):
        return self._age
        # using the setter method

    def set_age(self, a):
        self._age = a

    @property
    def age(self):
        return self._age


John = hanish()

# using the setter function
John.set_age(19)

# using the getter function
print(John.get_age())

print(John.age)
