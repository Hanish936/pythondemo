string=input(("Enter a letter:"))
if(string==string[::-1]):
      print("The letter is a palindrome")
else:
      print("The letter is not a palindrome")


num=int(input("Enter a number"))
temp=num
rev=0
while(num>0)
	dig=num%10
	rev=rev*10+dig
	num=num//10
if(temp==rev):
	print("tne number is palindrome")
else:
	print("the number is not palindrome")

#factorial
# program to find
# factorial of given number
def factorial(n):
	if (n == 1 or n == 0):
		return 1
	else:
		return n * factorial(n - 1);

num = int(input("Enter a number"));
print("Factorial of", num, "is",
	  factorial(num))
#fibonacci
# Function for nth Fibonacci number
def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")
	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0
	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(9))
#aramstroong number
number = int(input("Enter a number"))
temp = number
add_sum = 0
while temp!=0:
    k = temp%10
    add_sum +=k*k*k
    temp = temp//10
if add_sum==number:
    print('Armstrong Number')
else:
    print('Not a Armstrong Number')

