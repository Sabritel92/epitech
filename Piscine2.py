print("Task 1.1")
print(1+1)
print(30+12)
print(777+(-735))
print(1+2+3+5+7+11+13)

print("\n Task 1.2")
print(84-42)
print(0-(-42))
print(2*21)
print((-6)*(-7))
print(2+5*8)
print((3+(3*4-2*2)*3-2)*2-3)

print("\n Task 1.3")
print(84/2)
print(84//2)
print("84/2 met la valeur en entière et 84//2 en quotient")

print("\n Task 1.4")
'print(84/(8+(-3)+(-7)+2))'
print("Avec ce calcul, on essaie de diviser 84 par 0, ça produit une erreur comme il est impossible à résoudre")

print("\n Task 2.1")
print(1+11+111+1111+11111+111111+1111111+11111111+111111111)
print((1+11+111+1111+11111+111111+1111111+11111111+111111111)^2)
print((1+11+111+1111+11111+111111+1111111+11111111+111111111)^3)
print((1+11+111+1111+11111+111111+1111111+11111111+111111111)^4)
print((1+11+111+1111+11111+111111+1111111+11111111+111111111)^5)

print(1+11+111+1111+11111+111111+1111111+11111111+111111111+1111111111)
print((1+11+111+1111+11111+111111+1111111+11111111+111111111+1111111111)^2)
print((1+11+111+1111+11111+111111+1111111+11111111+111111111+1111111111)^3)
print((1+11+111+1111+11111+111111+1111111+11111111+111111111+1111111111)^4)
print((1+11+111+1111+11111+111111+1111111+11111111+111111111+1111111111)^5)

print("\n Task 2.2")
print(17^1024)

print("\n Task 3.1")
print(42/4)
print(42//4)
print(42%4)

print("\n Task 3.2")
'''num=int(input("Choose a number :"))
if (num % 2) == 0:
    print(num," is Even")
else:
    print(num," is Odd")
'''

print("\n Task 3.3")
print(sum([1,2,3,4,3,4,5,6,5]))
print(sum([3,4,5,5,6,7,4,2,6]))
print(sum([4,4,4,9,0,3,2,0,0,9,7]))

print("\n Task 3.4")
print(12.24 // 1)
print(424242.8412 // 1)

print("\n Task 3.5")
print(12.24 % 1)
print(424242.8412 % 1)

print("\n Task 4.1")
'''t=1
d=1
pi6deci=3.141592
pi=0

while round(pi, 6) != pi6deci:
    pi+=4*(t/d)
    d+=2
    t=-t
    print(round(pi, 6))
'''
print("\n Task 4.2")
pi=0.141592    
d=1
x=1
t=6
suite=1
while round(pi, 6) != x:
    suite=t+(d^2)/suite
    pi+=(d^2)/suite
    d+=2
    print(round(pi, 6))
