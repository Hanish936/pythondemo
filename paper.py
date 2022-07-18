	#string1='hanish singh';
	#print(string1[::-1])
	#string2='hanish singh chauhan';
	#print(string2[::2])
	#print(string2)
	##Printing hello in octal
	#String1 = "\110\145\154\154\157"
	#print("\nPrinting in Octal with the use of Escape Sequences: ")
	#print(String1)

	# Using raw String to
	# ignore Escape Sequences
	#String1 = r"This is \110\145\154\154\157"
	#print("\nPrinting Raw String in Octal Format: ")
	#print(String1)

	# Printing Geeks in HEX
	#String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
	#print("\nPrinting in HEX with the use of Escape Sequences: ")
	#print(String1)

	# Using raw String to
	# ignore Escape Sequences
	#String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
	#print("\nPrinting Raw String in HEX Format: ")
	#print(String1)

	#This code is updated by Susobhan Akhuli
	#def my_function():
		#'''Demonstrates triple double quotes
		#docstrings and does nothing really.'''

		#return None

	#print("Using __doc__:")
	#print(my_function.__doc__)

	#print("Using help:")
	#help(my_function)

list1=[["harry",1],["marie",2],["human",3]]
dict1=dict(list1)
for item,lolipop in dict1.items():
	print(item,lolipop)


def function1(a,b):
	avg=a+b/2
	return avg

v=function1(5,7)
print(v)
h=open("new.txt")
f=h.read(34455)
print("1",f)
h=open("new.txt")
f=h.read(34455)
print("2",f)
h=open("new.txt")
for line in h:
	print(line,end="")
print(f)
f=open("new.txt",'a')
a=f.write("harry bhai bhut ache hain")
print(a)
f.close()
num = int(input("enter no.of rows uh want to print: "))
for i in range(1,num+1):
	print("*"*i)
