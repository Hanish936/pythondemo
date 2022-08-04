FILE
HANDLING...................................................................
"""
:::::jdo
data
permanent
store
krnaa
ta
files
vala
concept
use
kr
skde
fxn
"""
#open(filename, mode)

#eg: print('print')

f = open('test1.txt', 'r+')
f.write("Good Morning")
f.writelines(["komal\n", "meena\n", "shanti\n"])
print(f.read())

# print(f.read(5))

# print('char',f.read(5))

f.close()
t = open('demo.txt', 'r')
# print('char',t.read())


eg2::  f = open('test.txt', 'a')
f.writelines(["suman", "jatinder"])
f.close()
g = open('test.txt', 'r')
print(g.read(5))
g.seek(0)
print(g.read(10))