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