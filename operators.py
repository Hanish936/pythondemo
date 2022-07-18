#arthematic operators
# +,-,*,/,//,**,%
#realtional operator
#<,>,<=,>=,!=,==,=
#logical
#and,or,not
#bitwise
#&(bitwise and ),|(bitwise or),^(bitwise and),>>(left shift ),<<(right shift),~(complemnt)x
a=5
b=5
print(a+b)
print(a-b)
print(a/b)
print(a//b)
print(a%b)
#relational
x = 5
y = 3

print(x == y)
x = 5
y = 3

print(x != y)
x = 5
y = 3

print(x > y)
x = 5
y = 3

print(x < y)
x = 5
y = 3

print(x >= y)
x = 5
y = 3

print(x <= y)
#logical
x = 5

print(x > 3 and x < 10)
x = 5

print(x > 3 or x < 4)
x = 5

print(not(x > 3 and x < 10))
a = 33
b = 200
#bitwise
# Python program to show
# bitwise operators

a = 10
b = 4

# Print bitwise AND operation
print("a & b =", a & b)

# Print bitwise OR operation
print("a | b =", a | b)

# Print bitwise NOT operation
print("~a =", ~a)

# print bitwise XOR operation
print("a ^ b =", a ^ b)

if b > a:
  print("b is greater than a")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  a = 200
  b = 33
  if b > a:
      print("b is greater than a")
  elif a == b:
      print("a and b are equal")
  else:
      print("a is greater than b")
i = 1
while i < 6:
  print(i)
  i += 1
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
#pattern
for i in range(4):
    for j in range(4):
        print("* ", end="")
    print()

for x in range(5):
    for y in range(x):
        print("*",end="")
    print()


def insert_sting_middle(str, word):
    length = len(str)
    loc = length//2
    return str[:loc] + word + str[loc:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
    # number of spaces
    k = n - 1

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


# Driver Code
n = 5
triangle(n)





