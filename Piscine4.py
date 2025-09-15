print("Task 1.1")
'''(42>12) 42 est supérieur à 12
    (12=12) 12 devient 12
    (12==12) 12 est égale à 12
    ("hello" == "world") "hello" est égale à "world" 
    (218 >= 118) 218 est supérieur ou égale à 118
    ("a".upper() == "A") "a".upper() est égale à "A"
    (1*2*3*4 <= 9) 1*2*3*4 est inférieur ou égale à 9
    ("z" in "azerty") "z" est présent dans "azerty" donc envoie la valeur True
'''

print("Task 1.2")
'''x=int(input("Integer: "))
if (x==42):
    print("This is correct!")
else:
    print("It's incorrect!")'''

print("Task 1.3")
'''num=int(input("Integer :"))
if (num % 2) == 0:
    print(num,"This integer is even")
else:
    print(num,"This integer is odd")'''

print("Task 1.4")
'''string=input("Magic key :")
if string=="open sesame":
    print("access granted")
else:
    if string=="will you open, you goddamn !":
        print("access fucking granted")
    else:
        print("permission denied")'''

print("Task 1.5")
'''y=int(input("Integer: "))
for i in range(1):
    if (y==42):
        print("a")
    elif (y<=21):
        print("b")
    elif (y%2)==0:
        print("c")
    elif (y/2)<21:
        print("d")
    elif (y%2)!=0 & y>=45:
        print("e")
    else:
    print("f")'''

print("Task 1.6")
'''a = 42
b = 41
if a == b:
    print ("A and B is the sames ")
if b <= a:
    print ("B is equal or lower as A")
if b != a:
    print ("B his diferent from A")'''

print("Task 2.1")
'''i=0
for i in range(1000):
    i=i+1
    print(i)'''

print("Task 2.2")
'''user_input = input("Enter word: ")
result = ""
for char in user_input:
    result += char * 2
print(result)'''

print("Task 2.3")
'''for i in range(10000, 0, -1):
    if i % 7 == 0:
        print(i)'''

print("Task 2.4")
'''for i in range(-30, 30):
    if i % 3 == 0 & i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)'''

print("Task 2.5")
'''for bottles in range(99, 0, -1):
    if bottles>1:
        print(bottles,"bottles of beer on the wall, "+str(bottles)+" bottles of beer.")
        if bottles-1==1:
            print("Take one down and pass it around, 1 bottle of beer on the wall.\n")
        else:
            print("Take one down and pass it around, "+str(bottles - 1)+" bottles of beer on the wall.\n")
    else:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")'''

print("Task 2.6")
'''n = int(input("Enter an integer n: "))
for i in range(2, n//2+1):
    print("")
    for m in range(n-1, i-1, -1):
        if (m%i)==0:
            print(m, end=" ")'''

print("Challenge")
'''n=int(input("Enter an integer: "))
s=input("Enter a string: ")
for i in range(1):
    if (n==0):
        quit()
    elif any(vowel in s for vowel in "aeiouyAEIOUY"):
        print(n)
    elif (n>=42):
        print(n)
    else:
        print(s)'''

print("Task 3.1")
'''message=input("Enter a message: ")
key=int(input("Enter a key (1-26): "))
encrypted_message=""
for i in message:
    encrypted_message=chr((ord(i)-ord('a')+key)%26+ord('a'))
    encrypted_message+=i
print(encrypted_message, end="")'''

print("Task 3.2")
ciphered = input("Enter the encrypted message: ")
key = int(input("Enter the key (1-26): "))
decrypted = ""

for i in ciphered:
    if i.isalpha():
        decrypted+=chr((ord(i)-ord('a')-key)%26+ord('a'))
    else:
        decrypted+=i
print(decrypted)

print("Task 3.3")
