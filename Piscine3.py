
print("Task 1.1")
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(a)

print("Task 1.2")
print(a[0])
print(a[12])

print("Task 1.3")
print(a[-1])

print("Task 1.4")
print(a[4],a[9])

print("Task 2.1")
a_lower=a.lower()
print(a_lower)

print("Task 2.2")
b="tutu on the tuki-kata"
print(b.replace("tu","ta"))

print("Task 2.3")
'''Il va chercher dans la chaîne de caractère un "a" et afficher la position du mot ou de la lettre choisi, dans ce cas présent il y en a pas alors il va simplement afficher une valeur négative'''
string="Hello world !"
position=string.find("a")
print(position)

print("Task 2.4")
''''''
p = "abcdefghij"
print (p [:: -2][:5][:: -1][3:])

print("Task 2.5")

print("Task 2.6")
for x in range(10):
    print(a)

print("Task 2.7")
print("hello"+ str( 42))

print("Task 2.8")
s1, s2, s3='"42',"is",'the answer"'
print(s1,s2,s3+" contains "+str(len(s1+s2+s3))+" characters.")

print("Task 3.1")
'''username=input("What is your username?")
print("Hello "+username+"!")'''

print("Task 3.2")
'''print(input("Choose a number"))'''

print("Task 3.3")
'''a1=int(input("Choose a number 1"))
a2=int(input("Choose a number 2"))
x1=(a1+a2)
print("The sum of the provided numbers is "+str(x1))'''

print("Task 3.4")
string=input("Type a string")
s_list=string.split()
for word in s_list:
    print(word[0])