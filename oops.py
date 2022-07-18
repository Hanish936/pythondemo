
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec
@dec1
def who_is_harry():
    print("Harry is a good boy")
who_is_harry()
def inner1(func):
    def inner2():
        print("Before function execution");
        func()
        print("After function execution")
    return inner2

@inner1
def function_to_be_used():
    print("This is inside the function")
function_to_be_used()
class student:
    def __init__(self , name , rollno , std):
        self.id=name
        self.roll=rollno
        self.divison=std

   # def children(self):
     #   return f"this is my name {self.id} my roolno is {self.roll} division is {self.divison}"

harry=student("hanish",17,"btech")
carry=student("carry",12,"btech")
print(harry.id)

