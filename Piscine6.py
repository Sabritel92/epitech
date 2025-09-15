print("Task 1.1")
# a retourne 42 et b retourne 52
'''def f1 () :
    return 42
def f2 (x):
    return 2 * x
print ( f1 () )
print ( f2 (5) + f1 () )'''

print("Task 1.2")
'''def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print (" O O O O O O")
def ham () :
    print (" ============ ")'''
# print((bread (), lettuce (), tomato (), ham (), lettuce (), tomato (), ham(), bread ()))

print("Task 1.3")

'''def double_sandwich ():
    bread ()
    lettuce ()
    tomato ()
    ham ()
    lettuce ()
    tomato ()
    ham()
    bread ()

for i in range (4):
    print(double_sandwich())'''

print("Task 1.4")
'''
n=int(input("Choose how many sandwich do you want: "))
if n<0:
    print("I can't do this!")

for i in range (n):
    print(double_sandwich())'''

print("Task 1.5")

'''def vegetable():
    print(" ^^^^^^^^^^^^ ")

def veg_sandwich():
    bread()
    lettuce() 
    tomato()
    vegetable()
    vegetable()
    bread()

n=int(input("Choose how many sandwich do you want: "))
if n<0:
    print("I can't do this!")
v=input("Do you want a vegetable sandwich? (yes/no): ")
if v=="yes":
    for i in range (n):
        print(veg_sandwich())
else:
    for i in range (n):
        print(double_sandwich())'''

print("Challenge")
def f1():
    return 42

def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

import time
start = time.time()
print(power(f1(), 84))
print(power(f1(), 168))
print(time.time() - start)

print("Task 2.1")
def n():
    return 42
result=0
for i in range(n()):
    result+=i+1
print(result)

print("Task 2.2")

# Write a recursive function that prompt the user for a string of characters, strip out the spaces and punctu-
# ation signs, lowercase the string, then test if is a palindrome.
# It should return ”True” for never odd or even and A Santa Lived As a Devil at NASA.

'''s=input("Enter a string: ")
def palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
print(is_palindrome(s))'''

print("Task 2.3")
'''Write a program that lists all the files and directories in the current directories, as well as all files and
directories in its sub-directories and so on.
It should behave similarly as the ls -R command.'''
'''import os
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
list_files('.')'''

print("Task 3.1")
s=input("Enter a string: ")
n=int(input("Enter a number: "))
def funA(s, n):
    i=0
    characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for j in s:
        if j in characters:
            i+=1
        if i>=n:
            return True
    return False
def funB(s, n):
    i=0
    special_characters="!@#$%^&*()-+?_=,<>/àéèçâêîôûäëïöü.;:[]|`~§µ£¤€²³"
    for j in s:
        if j in special_characters:
            i+=1
        if i>=n:
            return True
        
    return False
def funC(s, n):
    i=0
    numbers="0123456789"
    for j in s:
        if j in numbers:
            i+=1
        if i>=n:
            return True
    return False
        
print("funA:", funA(s, n))
print("funB:", funB(s, n))
print("funC:", funC(s, n))

print("Task 3.2")
def passcheck(fun, n, s):
    if fun(s, n):
        if fun==funA and n<=16:
            print("Password is valid")
        if fun==funB and n<=3:
            print("Password is valid")
        if fun==funC and n<=1:
            print("Password is valid")
    else:
        print("Password is invalid")
    
passcheck ( funA , 16 , s)
passcheck ( funB , 3, s)
passcheck ( funC , 1, s)

print("Task 3.3")
# Add error handling to your previous function.
# A common misuse would be providing input of the wrong type (integer, boolean, string, ...).
try:
    passcheck ( funA , 16 , s)
    passcheck ( funB , 3, s)
    passcheck ( funC , 1, s)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except TypeError:
    print("Invalid input type. Please enter a valid string.")
except:
    print("An unexpected error occurred.")