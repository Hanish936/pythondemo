#Dictionary is nothing but a key value pair.
#for dictionary we use {}.
D1={}
print(type(D1))
D2={"Harry":"Burger","Rohan":"fish","sham":"egg"}
print(D2["Harry"])
D2={"Harry":"Burger","Rohan":"fish","sham":{"B":"baseball","C":"cricket","D":"dance"}}
D2["Ankit"]="Noodles"
D2[420]="kebabs"
# del D2["Ankit"]
# del D2[420]
#D3=D2
#del D3["Harry"] It will delete harry from D2 becuse d3 is referncing D2 not storing the data of d2 works as pointer
D3=D2.copy() #here we are making copy of D2 in D3
del D3["Harry"]
D2.update({"leena":"toffe"})#we can also use that for update
print(D2.get("Harry"))#we can also use this for fetiching the data
print(D2.keys())
print(D2.items())
var1=int(input("enter the number"))
var2=int(input("enter the number"))