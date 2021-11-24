def menu():
    print('1. Odrátanie')
    print('2. Sčítanie')
    print('3. Násobenie')
    print('4. Delenie')
    print('5. Koniec')
    volba = input('Tvoja volba: ')
    return int(volba)

def odratanie():
    a = int(input('Zadaj prvé číslo: '))
    b = int(input('Zadaj druhé číslo: '))
    return print(f'{a} - {b} = {a - b}')


def scitanie():
    a = int(input('Zadaj prvé číslo: '))
    b = int(input('Zadaj druhé číslo: '))
    return print(f'{a} + {b} = {a + b}')

def nasobenie():
    a = int(input('Zadaj prvé číslo: '))
    b = int(input('Zadaj druhé číslo: '))
    return print(f'{a} * {b} = {a * b}')

def delenie():
    a = int(input('Zadaj prvé číslo: '))
    b = int(input('Zadaj druhé číslo: '))
    return print(f'{a} / {b} = {a / b}')

volba = 0
a = 0
b = 0

while volba != 5:
    volba = menu()
    if volba == 1:
        odratanie()
    elif volba == 2:
        scitanie()
    elif volba == 3:
        nasobenie()
    elif volba == 4:
        delenie()
