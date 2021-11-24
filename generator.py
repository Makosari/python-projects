import time, random


def menu():
    print('1. Generátor pseudonáhodných čísel')
    print('2. Hod dvoma kockami')
    print('3. Generátor hesiel')
    print('4. Koniec')
    volba = int(input('Tvoja voľba: '))
    return volba


# konstanty
a = 25173
b = 13849
c = 65536


def generuuj(y, a, b, c):
    y = (y*a+b) % c                                     #kazde dalsie y sa vypocita z predchadzajuceho
    return y


def generator1():
    cas = str(time.time())
    cas = int(cas[-3:])
    x = cas
    p = []
    pocet = int(input('Zadaj počet generovaní: '))
    minimum = int(input('Zadaj dolnú hranicu: '))
    maximum = int(input('zadaj hornú hranicu: '))
    for i in range(maximum+1):
        p.append(0)
    for i in range(pocet):
        x = generuuj(x, a, b, c)
        v = (x/c * (maximum - minimum + 1) + minimum)
        v = int(v)
        p[v] += 1
        print(v, end=', ')
    print()
    for i in range(minimum, maximum + 1):
        print(i, ': ', p[i])


def kocky():
    pocet = int(input('Zadaj počet hodov: '))
    # python generator
    cisla1_ran = []
    cisla2_ran = []
    vysledky_ran = []
    for i in range(pocet):
        cisla1_ran.append(random.randint(1, 6))
        cisla2_ran.append(random.randint(1, 6))
    for i, k in zip(cisla1_ran, cisla2_ran):
        print(f'{i} + {k}', end=' | ')
        vysledky_ran.append(i + k)
    print()
    z = 2
    for i in range(2, 13):
        print(f'{z} : {vysledky_ran.count(i)}')
        z += 1
    print('-------------------------------------Môj generátor-------------------------------------------')
    #zaciatok mojho  generatora
    cisla1 = []
    cisla2 = []
    vysledky = []
    x = 1
    minimum = 1
    maximum = 6
    for i in range(pocet):
        x = generuuj(x, a, b, c)
        v = (x / c * (maximum - minimum + 1) + minimum)
        v = int(v)
        cisla1.append(v)
    for i in range(pocet):
        x = generuuj(x, a, b, c)
        v = (x / c * (maximum - minimum + 1) + minimum)
        v = int(v)
        cisla2.append(v)
    for i, k in zip(cisla1, cisla2):
        print(f'{i} + {k}', end=' | ')
        vysledky.append(i+k)
    print()
    z = 2
    for i in range(2, 13):
        print(f'{z} : {vysledky.count(i)}')
        z += 1


def generator_hesiel():
    pocet = int(input('Zadaj počet hesiel: '))
    pismena_male = 'abcdefghijklmnopqrstuvwxyz'
    cisla = '0123456789'
    znaky = '+-*'
    f = pismena_male.upper()
    for i in range(pocet):
        heslo = random.choice(znaky) + random.choice(f) + random.choice(cisla)
        for i in range(5):
            heslo += random.choice(pismena_male)
        heslo = list(heslo)
        random.shuffle(heslo)
        op = 1
        for i in heslo:
            print(i, end='')
            op += 1
        print()


volba = 0
while volba != 4:
    volba = menu()
    if volba == 1:
        generator1()
    elif volba == 2:
        kocky()
    elif volba == 3:
        generator_hesiel()
