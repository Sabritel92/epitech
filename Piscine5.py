print("Task 1.1")
list=[1, 2, 3, 4, 5]
print(list[1])

print("Task 1.2")
print(list[-1])

print("Task 1.3")
list.append(42)
list.append("forty-two")

print("Task 1.4")
print(list)
for element in list:
    print(element)

print("Task 1.5")
list.pop()
print(list)

print("Task 1.6")
list.insert(0, 0)
print(list)

print("Task 1.7")
print(list[1:4])

print("Task 1.8")
list.reverse()
print(list)

print("Task 1.9")
print(list[::2])

print("Task 1.10")
for i in range(11, 22):
    list.append(i)
print(list)

print("Task 1.11")
my_first_list = [4 , 5, 6]
my_second_list = [1 , 2, 3]
my_first_list . extend ( my_second_list )
print ( my_first_list )
# Ce code permet d'ajouter my_first_list à my_second_list

my_first_list = [7 , 8, 9]
my_second_list = [4 , 5, 6]
my_first_list = [* my_first_list , * my_second_list ]
print ( my_first_list )
# Ce code renvoie le même résultat que le code précédent mais n'a pas la même forme

print("Task 2.1")
list2=[1, 2, 3, 4, 5]
result = 1
for num in list2:
    result *= num
print(result)

print("Task 2.2")
print([x + 10 for x in [3, 2, 6, 7, 1, 4]])
# Ce code ajoute 10 à chaque élément de la liste

print("Task 2.3")
'''list(filter(lambda x: x > 10, [42, 3, 4, 7]))'''
# Ce code filtre les éléments de la liste pour ne garder que ceux qui sont supérieurs à 10

print("Task 2.4")
list3=[4, 8, 2, 7, 5]
print(min(list3))
print(max(list3))

print("Task 2.5")
print(reversed(sorted(list3)))

print("Task 2.6")
print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])
# Ce code divise par 2 les éléments pairs et multiplie par 2 les éléments impairs

print("Task 2.7")
print([*enumerate([42, 3, 4, 18, 3, 10])])
# Ce code affiche chaque élément de la liste et les énumère

print("Task 2.8")
first_names = [" Jackie " , " Chuck " , " Arnold " , " Sylvester "]
last_names = [" Stallone " , " Schwarzenegger " , " Norris " , " Chan "]
magic = [* zip ( first_names , last_names [:: -1]) ]
print ( magic [0])
print ( magic [3])
print ( magic [1][0])
print ( magic [0][1])
print ( magic [2])

# Ce code crée une liste pour le prénom et nom de famille, crée une variable magique qui combine les deux listes en inversant l'ordre des noms de famille, puis affiche les éléments demandés

print("Challenge")
'''import time
start = time.time()
import random
list4=[random.randint(1, 1000000) for _ in range(1000000)]
list4.sort()
print(list4)
print(time.time()- start)'''

print("Task 3.1")
studient = {
    "player": "Donovan",
    "team": "Pre Msc",
}
print (studient["player"])
print (studient["team"])

print("Task 3.2")
superheroes = {
    " Batman " : {
        " id ": 1,
        " aliases ": [" Bruce Wayne " , " Dark knight "],
        " location ": {
            " number " : 1007 ,
            " street ": " Mountain Drive " ,
            " city ": " Gotham "
            }
    },
    " Superman " : {
        " id ": 2,
        " aliases ": [" Kal - El " , " Clark Kent " , " The Man of Steel "],
        " location ": {
            " number " : 344 ,
            " street ": " Clinton Street " ,
            " apartment ": "3D" ,
            " city ": " Metropolis "
            }
    },
}
print (superheroes[" Superman "][" location "][" city "])

print("Task 3.3")
superheroes2 = {
    " Batman " : {
        " id ": 1,
        " aliases ": [" Bruce Wayne " , " Dark knight " , " Caped Crusader "],
        " location ": {
            " number " : 1007 ,
            " street ": " Mountain Drive " ,
            " city ": " Gotham "
            }
    },
    " Superman " : {
        " id ": 2,
        " aliases ": [" Kal - El " , " Clark Kent " , " The Man of Steel "],
        " location ": {
            " number " : 344 ,
            " street ": " Clinton Street " ,
            " apartment ": "3D" ,
            " city ": " Metropolis "
            }
    },
}

print("Task 3.4")
dict = {
    " dalmatians ": 101 ,
    " pi ": 3.14 ,
    " beast ": 3*2*111 ,
    " life ": 42 ,
    " googol ": 10^100
}
print(max(dict, key=dict.get))

print("Task 4.1")
'''name_list=["Alice", "Bob", "Charlie"]
name=input("Enter your name: ")
if name in name_list:
    print("welcome in")
else:
    print("get lost!")'''

print("Task 4.2")
duplicate_list=[1, 1, 2, 2, 3]
duplicate_list2=['a', 2, 'a', 2, 'A']
not_duplicate_list=[]
not_duplicate_list2=[]
for i in duplicate_list:
    if i not in not_duplicate_list:
        not_duplicate_list.append(i)
for j in duplicate_list2:
    if j not in not_duplicate_list2:
        not_duplicate_list2.append(j)
print(not_duplicate_list)
print(not_duplicate_list2)

print("Task 4.3")
meeting={
    " Monday ": {
        "3:30 PM": [" Joe " , " Sam "],
        "4:30 PM": [" Bob " , " Alice "]
    },
    " Tuesday ": {
        "3:30 PM": [" Joe " , " Bob " , " Alice " , " Sam "],
        "9:30 AM": [" Joe " , " Bob "]
    }
}
for day, times in meeting.items():
    for time, people in times.items():
        if " Joe " in people:
            print("Joe", day, time)
