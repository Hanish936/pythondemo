#list in pyhton
#lists can be modified(mutable=can change)
#in list we have square brackets[]
mylist = ["a", "b", "c", "a"]
print(mylist)
print(len(mylist))
print(type(mylist))

#access item
print(mylist[1])

#change item
mylist[1] = "hello"
print(mylist)

#add item
mylist.append("world")
print(mylist)

#insert item
mylist.insert(1, "hi")
print(mylist)

#remove list
mylist.remove("a")
print(mylist)

#pop item
mylist.pop(1)
print(mylist)

mylist.pop()
print(mylist)


# for loop
for x in mylist:
  print(x,end=" ")

#sort item
print(mylist.sort())
grocery = ["harpic", "bhindi", "shampoo", "toothpaste", "lolipop"]
#print(grocery[0])
numbers = [2,5,3,7,4,8]
numbers.sort()
numbers.reverse()
#print(numbers)
#a=1
#b=2
#a,b=b,a
#print(a,b)

#tuple in pyhton
#tuple cant be modified as list(immutable)
#In tuples we have paranthesis()
grocery = ("harpic", "bhindi", "shampoo", "toothpaste", "lolipop")
print(type(grocery))
#tuple
mytuple = ("a", "b", "c", "b")
print(mytuple)
print(len(mytuple))
print(type(mytuple))

#access tuple
print(mytuple[1])

#change tuple items
x = list(mytuple)
x[1] = "hello"
print(tuple(x))

#add item
x = list(mytuple)
x.append("world")
print(tuple(x))

#remove item
x = list(mytuple)
x.remove("b")
print(tuple(x))

#foor loop
for x in mytuple:
  print(x, end=" ")
print(" ")

#count item
print(mytuple.count("b"))

#index item
print(mytuple.index("b"))

#sets
myset = {"a", "b", "c", "a"}
print(myset)
print(len(myset))
print(type(myset))

# add item
myset.add("t")
print(myset)

#remove item
myset.remove("a")
print(myset)

#pop item
x = myset.pop()
print(x)
print(myset)

#for loop
for x in myset:
  print(x, end=" ")

#clear item
print(myset.clear())

#dict
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)
print(len(my_dict))
print(type(my_dict))

# access item
print(my_dict[2])
print(my_dict.get(1))

#changing item
my_dict[1] = "hello world"
print(my_dict)

#add item
my_dict[3] = "how are you"
print(my_dict)

#pop item
print(my_dict.pop(2))
print(my_dict)

#remove item
print(my_dict.popitem())
print(my_dict)

#clear item
print(my_dict.clear())
print(my_dict)

my_dict = {1: 'hello world', 2: 'ball', 3: 'how are you'}
#printing keys
print(my_dict.keys())
#printing values
print(my_dict.values())
#printing items
print(my_dict.items())

#functions
def functions():
    #statement
def sum()
    print(10+20)
sum()
def disp(a,b,c):
    d=a+b+c
    print(d)
disp(10,20,30)

def disp(a,b,c):
    d=a+b+c
    return d

h=disp(10,20,30)
print(h)