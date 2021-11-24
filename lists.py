import random


def menu():
    print("1) Nacitaj zoznam")
    print("2) Generuj zoznam")
    print("3) Linearne vyhladavanie")
    print("4) Binarne vyhladavanie")
    print("5) Triedenie vyberom")
    print("6) Triedenie vkladanim")
    print("7) Triedenie vymenou")
    print("8) Druha najvacsia hodnota")
    print("9) Koniec")
    vypis_zoznam(zoznam)
    volba = input("Tvoja volba: ")
    return int(volba)


def vypis_zoznam(zoznam):
    print(zoznam)


def nacitaj_zoznam(zoznam):
    pocet = int(input("Zadajte pocet prvkov zoznamu: "))
    zoznam = []
    for i in range(pocet):
        z =int(input("Zadajte hodnotu: "))
        zoznam.append(z)
    return zoznam


def generuj_zoznam(zoznam):
    pocet = int(input("Zadajte pocet prvkov zoznamu: "))
    zoznam = []
    for i in range(pocet):
        z = random.randint(0, 99)
        zoznam.append(z)
    return zoznam


def linearne_vyhladavanie(zoznam):
    hladane = int(input("Zadajte hladanu hodnotu: "))
    if hladane in zoznam:
        print(f'{hladane} sa nachádza v zozname na {zoznam.index(hladane)} mieste.')
    else:
        print(f'{hladane} sa v zozname nenachádza.')


def binarne_vyhladavanie(zoznam):
    hladane = int(input('Zadaj hladanu hodnotu: '))
    l = 0
    p = len(zoznam) - 1
    stred = 0
    if zoznam[0] < zoznam[-1]:
        while l <= p:
            stred = (l + p) // 2
            if zoznam[stred] == hladane:
                print(stred)
                return stred
            elif zoznam[stred] < hladane:
                l = stred + 1
            else:
                p = stred - 1
    elif zoznam[0] > zoznam[-1]:
        while l <= p:
            stred = (l + p) // 2
            if zoznam[stred] == hladane:
                print(stred)
                return stred
            elif zoznam[stred] > hladane:
                l = stred + 1
            else:
                p = stred - 1
    print('Hľadané číslo sa v zozname nenachádza')
    return -1


def tried_vyberom(zoznam):
    print('1) Usporiadať vzostupne \n2) Usporiadať zostupne  ')
    ako = int(input('Výber: '))
    if ako == 1:
        for i in range(len(zoznam)):
            min = i
            for j in range(i + 1, len(zoznam)):
                if zoznam[j] < zoznam[min]:
                    min = j
            zoznam[i], zoznam[min] = zoznam[min], zoznam[i]
    elif ako == 2:
        for i in range(len(zoznam)):
            min = i
            for j in range(i + 1, len(zoznam)):
                if zoznam[j] > zoznam[min]:
                    min = j
            zoznam[i], zoznam[min] = zoznam[min], zoznam[i]
    else:
        print('Niečo je zle!')


def tried_vkladanim(zoznam):
    print('1) Usporiadať vzostupne \n2) Usporiadať zostupne  ')
    ako = int(input('Výber: '))
    if ako == 1:
        for i in range(1, len(zoznam)):
            x = zoznam[i]
            j = i - 1
            while j >= 0 and x < zoznam[j]:
                zoznam[j + 1] = zoznam[j]
                j = j - 1
                zoznam[j + 1] = x
    elif ako == 2:
        for i in range(1, len(zoznam)):
            x = zoznam[i]
            j = i - 1
            while j >= 0 and x > zoznam[j]:
                zoznam[j + 1] = zoznam[j]
                j = j - 1
                zoznam[j + 1] = x
    else:
        print('Niečo bolo zle!')


def tried_vymenou(zoznam):
    print('1) Usporiadať vzostupne \n2) Usporiadať zostupne  ')
    ako = int(input('Výber: '))
    if ako == 1:
        n = len(zoznam)
        for i in range(n):
            for j in range(0, n - i - 1):
                if zoznam[j] > zoznam[j + 1]:
                    zoznam[j], zoznam[j + 1] = zoznam[j + 1], zoznam[j]
    elif ako == 2:
        n = len(zoznam)
        for i in range(n):
            for j in range(0, n - i - 1):
                if zoznam[j] < zoznam[j + 1]:
                    zoznam[j], zoznam[j + 1] = zoznam[j + 1], zoznam[j]
    else:
        print('Niečo bolo zle!')


def druha_najvyssia_hodnota(zoznam):
    uniques = []
    for i in zoznam:
        if i not in uniques:
            uniques.append(i)
    uniques.sort()
    print(uniques[-2])


volba = 0

zoznam = []
while volba != 9:
    volba = menu()
    if volba == 1:
        zoznam = nacitaj_zoznam(zoznam)
    elif volba == 2:
        zoznam = generuj_zoznam(zoznam)
    elif volba == 3:
        linearne_vyhladavanie(zoznam)
    elif volba == 4:
        binarne_vyhladavanie(zoznam)
    elif volba == 5:
        tried_vyberom(zoznam)
    elif volba == 6:
        tried_vkladanim(zoznam)
    elif volba == 7:
        tried_vymenou(zoznam)
    elif volba == 8:
        druha_najvyssia_hodnota(zoznam)
    else:
        print('Niečo bolo zle!')
print("Dovidenia nabuduce")
