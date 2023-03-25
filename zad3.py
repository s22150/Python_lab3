import getpass
import random


def gra(choice1, choice2):
    if choice1 == 1:
        if choice2 == 3:
            return 1

    if choice1 == 2:
        if choice2 == 1:
            return 1

    if choice1 == 3:
        if choice2 == 2:
            return 1
    return 2


ilosc_rund = int(input("Wprowadz ilosc rund "))
list_zwyciestw = []
print(" wybrana ilosc rund = ", ilosc_rund)
typ_gry = int (input("Wprowadz typ gry (1 - computer, 2 - hot seats) "))
print("wybrany typ gry = " , typ_gry)
name1 = input("Wprowadz imie gracza 1 ")
name2 = "computer"

if typ_gry == 2:
    name2 = input("Wprowadz imie gracza 2")
    for i in range(ilosc_rund):
        print("1.nozyce")
        print("2.kamien")
        print("3.papier")
      #choice1 = int(getpass.getpass("wybor")) # nie dziala jezeli uruchamiach przez IDE
       # choice2 = int(getpass.getpass("wybor"))
        choice1 = int(input("wybor"))
        choice2 = int(input("wybor"))
        list_zwyciestw.append(gra(choice1, choice2))
else:
    for i in range(ilosc_rund):
        print("1.nozyce")
        print("2.kamien")
        print("3.papier")
       # choice1 = int(getpass.getpass("wybor"))
        choice1 = int(input("wybor"))
        choice2 = random.randint(1,3)
        list_zwyciestw.append(gra(choice1, choice2))
print(list_zwyciestw)

if list_zwyciestw.count(1) > list_zwyciestw.count(2):
    print("Gracz 1 zwyciezca")
elif list_zwyciestw.count(1) == list_zwyciestw.count(2):
    print("wygrała przyjaźń")
else:
    print("Gracz 2 zwyciezca")
