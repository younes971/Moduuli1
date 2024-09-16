

import random

n = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for i in range(n):
    heitto = random.randint
    summa += heitto

print(f"Arpakuutioiden silmälukujen summa on: {summa}")






luku = 13

for nimittaja in range(2, luku):
    print(nimittaja)
    if luku % nimittaja == 0:
        print("ei ole alkuluku")



luku = 20
alkuluku = "on alkuluku"
for nimittaja in range(2, luku):
    print(nimittaja)
    if luku % nimittaja == 0:
        alkuluku = "ei ole alkuluku"


    print(f" luku {alkuluku}")






kaupungit = []


for i in range(5):
    kaupunki = input(f"Anna kaupungin nimi {i+1}: ")
    kaupungit.append(kaupunki)

print("\nSyöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)





