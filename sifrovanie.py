def menu():
    print('1) Cézarova šifra - šifrovanie')
    print('2) Cézarova šifra - dešifrovanie')
    print('3) Cézarova šifra - šifrovanie s posunom')
    print('4) Cézarova šifra - dešifrovanie s posunom')
    print('5) Dešifrovanie súboru')
    print('6) Vigenerova šifra - šifrovanie s heslom')
    print('7) Vigenerova šifra - dešifrovanie s heslom')
    print('8. koniec')
    volba = int(input('Tvoja voľba: '))
    return volba


def cezar_sifruj():
    text = input('Zadaj text na sifrovanie: ')
    output = ''
    for i in text:
        output += chr(ord(i) + 3)
    print(output)


def cezar_desifruj():
    text = input('Zadaj sifru na desifrovanie: ')
    output = ''
    for i in text:
        output += chr(ord(i) - 3)
    print(output)


def sifruj_s_posunom():
    posun = int(input('Zadaj velkost posunu: '))
    text = input('Zadaj text na sifrovanie: ')
    output = ''
    for i in text:
        output += chr(ord(i) + posun)
    print(output)


def desifruj_s_posunom():
    posun = int(input('Zadaj velkost posunu: '))
    text = input('Zadaj sifru na desifrovanie: ')
    output = ''
    for i in text:
        output += chr(ord(i) - posun)
    print(output)


def desifrovanie_textu():
    ciselka = []
    ciselka_2 = []
    with open('sifra.txt', encoding='utf8') as f:
        for i in f:
            for k in i:
                ciselka.append(ord(k))
    counter = 0
    num = ciselka[0]
    for i in ciselka:
        curr_frequency = ciselka.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    space = ord(' ')
    cislo = num - space
    for i in ciselka:
        print(chr(i - cislo), end=' ')
    print()


def sifrovanie_s_heslom():
    text = input('Zadaj text na sifrovanie: ')
    heslo = input('Zadaj heslo: ')
    output = ''
    for i in range(len(text)):
        a = len(heslo)
        output += chr(ord(text[i]) + ord(heslo[i % len(heslo)]))
    print(output)


def desifrovanie_s_heslom():
    text = input('Zadaj text na sifrovanie: ')
    heslo = input('Zadaj heslo: ')
    output = ''
    for i in range(len(text)):
        a = len(heslo)
        output += chr(ord(text[i]) - ord(heslo[i % len(heslo)]))
    print(output)


volba = 0
while volba != 8:
    volba = menu()
    if volba == 1:
        cezar_sifruj()
    elif volba == 2:
        cezar_desifruj()
    elif volba == 3:
        sifruj_s_posunom()
    elif volba == 4:
        desifruj_s_posunom()
    elif volba == 5:
        desifrovanie_textu()
    elif volba == 6:
        sifrovanie_s_heslom()
    elif volba == 7:
        desifrovanie_s_heslom()
