import random


def menu():
    print('1) Nacitaj tabulku')
    print('2) Generuj tabulku')
    print('3) Vynasobenie hodnot tabulky konstantou')
    print('4) Transponovanie')
    print('5) Otacanie vpravo')
    print('6) Otacanie vlavo')
    print('7) Sucet dvoch matic')
    print('8) Sucin dvoch matic')
    print('9) Gaussova eliminačná metóda')
    print('10) Koniec')
    vypis(tab)
    volba = input('Tvoj vyber: ')
    return int(volba)


def vypis(tab):
    for riadok in tab:
        for hodnota in riadok:
            print(hodnota, end=' ')
        print()


def nacitaj(tab):
    riadok_a = int(input('Zadajte pocet riadkov: '))
    stlpec_a = int(input('Zadajte pocet stlpcov: '))
    print()
    tab = []
    for riadok in range(riadok_a):
        riadok_1 = []
        for stlpec in range(stlpec_a):
            riadok_1.append(int(input(f'{stlpec + 1}. hodnota v {riadok + 1}. riadku: ')))
        tab.append(riadok_1)
    return tab


def generuj(tab):
    riadok_a = int(input('Zadajte pocet riadkov: '))
    stlpec_a = int(input('Zadajte pocet stlpcov: '))
    print()
    tab = []
    for riadok in range(riadok_a):
        riadok_1 = []
        for stlpec in range(stlpec_a):
            riadok_1.append(random.randint(1, 100))
        tab.append(riadok_1)
    return tab


def nasob(tab):
    konst = int(input('Zadaj cislo, ktorym chces nasobit: '))
    return [[j*konst for j in i] for i in tab]


def transponuj(tab):
    return [[tab[j][i] for j in range(len(tab))] for i in range(len(tab[0]))]


def otocenie_vpravo(tab):
    tabulka = zip(*tab[::-1])
    return [list(i) for i in tabulka]


def otocenie_vlavo(tab):
   tabulka = list(zip(*reversed(tab)))
   return [list(i)[::-1] for i in tabulka][::-1]


def sucet_dvoch_matic(tab):
    riadky = int(input('Zadaj pocet riadkov: '))
    stlpce = int(input('Zadaj pocet stlpcov/prvkov v riadku: '))
    tab2 = []
    st = []
    g = 0
    while g != riadky:
        for i in range(stlpce):
            a = random.randint(0, 9)
            st.append(a)
        tab2.append(st)
        st = []
        g += 1

    tab1riadky = len(tab)
    tab2riadky = len(tab2)
    tab1stlpce = len(tab[0])
    tab2stlpce = len(tab2[0])

    if tab1riadky != tab2riadky or tab1stlpce != tab2stlpce:
        return "ERROR: Matice musia byť rovnako veľké"

    tab3 = []
    riadky = []

    for i in range(0, tab1riadky):
        for j in range(0, tab2stlpce):
            riadky.append(0)
        tab3.append(riadky.copy())
        riadky = []

    for i in range(0, tab1riadky):
        for j in range(0, tab2stlpce):
            tab3[i][j] = tab[i][j] + tab2[i][j]
    print(f'{tab}\n {tab2}')

    return tab3


def sucin_dvoch_matic(tab):
    rozmer = int(input('Zadaj rozmer tabulky (pocet riadkov): '))
    tab2 = []
    st = []
    g = 0
    while g != rozmer:
        for i in range(rozmer):
            a = random.randint(0, 9)
            st.append(a)
        tab2.append(st)
        st = []
        g += 1

    tab1riadky = len(tab)
    tab2riadky = len(tab2)
    tab1stlpce = len(tab[0])
    tab2stlpce = len(tab2[0])

    if tab1riadky != tab2riadky or tab1stlpce != tab2stlpce:
        return "ERROR: Matice musia byť rovnako veľké"

    tab3 = []
    riadky = []

    for i in range(0, tab1riadky):
        for j in range(0, tab2stlpce):
            riadky.append(0)
        tab3.append(riadky.copy())
        riadky = []

    for i in range(rozmer):
        for j in range(rozmer):
            for k in range(rozmer):
                tab3[i][j] = tab3[i][j] + tab[i][k] * tab2[k][j]

    print(f'{tab}\n {tab2}')
    return tab3


def gauss(tab):
    for i in range(len(tab) - 1):
        for j in range(i + 1, len(tab)):
            if tab[j][i] != 0:
                d = - tab[i][i] / tab[j][i]
                for k in range(len(tab) + 1):
                    tab[j][k] = tab[j][k] * d + tab[i][k]
    if tab[len(tab) - 1][len(tab) - 1] == 0:
        if tab[len(tab) - 1][len(tab)] == 0:
            print('Nekonecne mnozstvo rieseni.')
        else:
            print('Nema ziadne riesenie.')
    else:
        korene = [0] * len(tab)
        for i in reversed(range(len(tab))):
            for j in reversed(range(i + 1, len(tab))):
                tab[i][len(tab)] = tab[i][len(tab)] - tab[i][j] * korene[j]
            korene[i] = tab[i][len(tab)] / tab[i][i]
        print('Korene sustavy rovnic: ')
        print(korene)
    return tab


volba = 0
tab = []
while volba != 10:
    volba = menu()
    if volba == 1:
        tab = nacitaj(tab)
    elif volba == 2:
        tab = generuj(tab)
    elif volba == 3:
        tab = nasob(tab)
    elif volba == 4:
        tab = transponuj(tab)
    elif volba == 5:
        tab = otocenie_vpravo(tab)
    elif volba == 6:
        tab = otocenie_vlavo(tab)
    elif volba == 7:
        tab = sucet_dvoch_matic(tab)
    elif volba == 8:
        tab = sucin_dvoch_matic(tab)
    elif volba == 9:
        tab = gauss(tab)
