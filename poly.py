import tkinter


def menu():
   print('1. Načítanie polynomickej funkcie')
   print('2. Výpočet funkčnej hodnoty')
   print('3. Hladaj koreňe')
   print('4. Numericke integrovanie')
   print('5. Derivácia')
   print('6. Vlastnosti funkcie')
   print('7. Vykresli graf')
   print('8. Koniec')
   vypis_funkciu(koef)
   volba = input('Tvoja volba: ')
   return int(volba)


def nacitaj_funkciu():
   n = int(input('Zadaj stupen polynomickej funkcie: '))
   koef = []
   for i in range(n + 1):
       z = (int(input('Zadaj koeficient: ')))
       koef.insert(0, z)
   return koef


def fx(koef, x):
   n = len(koef) - 1
   pom = 0
   for i in reversed(range(n + 1)):
       pom = pom + koef[i] * (x ** i)
   return pom


def hladaj_korene():
   a = float(input('Zadaj lavu hranicu: '))
   b = float(input('Zadaj pravu hranicu: '))
   eps = float(input('Zadaj presnost: '))
   korene = []

   if fx(koef, a) == 0:  # koren je a
       korene.append(a)
   while a + 2 * eps < b:
       if fx(koef, a) * fx(koef, a + 2 * eps) < 0:
           korene.append(a + eps)
       if fx(koef, a + 2 * eps) == 0:
           korene.append(a + 2 * eps)
       a += 2 * eps
   if fx(koef, a) * fx(koef, b) < 0:  # koren jemedzi a a b
       korene.append((a + b) / 2)
   if fx(koef, b) == 0:  # koren je b
       korene.append(b)
   if len(korene) == 0:
       print('Na danom ntervale sa korene nenachadzaju.')
   else:
       eps_na_string = str(eps)
       korene_1 = [round(num, len(eps_na_string)-2) for num in korene]
       print(f'korene su {korene_1}')
       print()
       eps2 = float(input('Zadaj novú presnosť  pre bisekciu'))
       eps2_na_string = str(eps2)
       korene_bisekcia = []
       for i in range(len(korene)):
           a = korene[i] - eps
           b = korene[i] + eps
           while (b-a) > 2 * eps2 and fx(koef, (a+b)/2) != 0:
               stred = (a+b) / 2
               if fx(koef, a) * fx(koef, stred) < 0:
                   b = stred
               else:
                   a = stred
           korene_bisekcia.append((a+b)/2)
           korene_bisekcia_1 = [round(num, len(eps2_na_string)-2) for num in korene_bisekcia]
       print(f'Korene po bisekcii su: {korene_bisekcia_1}')


def numericke(koef):
   a = int(input("Zadaj lavu hranicu: "))
   b = int(input("Zadaj pravu hranicu: "))
   d = int(input("Zadaj pocet dielikov: "))
   y = (b - a) / d
   x1 = a
   x2 = a

   obsah1 = 0
   for i in range(1, d + 1):
       obsah1 = obsah1 + abs(fx(koef, x1))
       x1 = x1 + y
   print("obdlznikova metoda: ", obsah1 * y)
   print(x1)

   obsah = abs(fx(koef, x2) / 2)
   x2 = x2 + y
   for i in range(2, d + 1):
       obsah = obsah + abs(fx(koef, x2))
       x2 = x2 + y
   obsah = obsah + abs(fx(koef, x2) / 2)
   print("Lichobeznikova metoda: ", obsah * y)


def derivacia(koef,b):
   der = []
   der_1 = []

   for i in koef:
       der.append(i)
       der_1.append(i)
   a = 1
   while len(der) != 1:
       for i in range(len(der)):
           der[i] = der[i] * i
       der.pop(0)
       print(f'{a}. derivácia:', end='')
       vypis_funkciu(der)
       a += 1
   print(f' výsledok derivácie = {der}')
   if b == 1:
       for i in range(1):
           der_1[i] = der_1[i] * i
       der_1.pop(0)
       return der_1


def vypis_funkciu(koef):
   print('f(x) = ', end='')
   for i in reversed(range(len(koef))):
       if koef[i] != 0:
            if (i + 1) == len(koef) or koef[i] < 0:
                if koef[i] == -1 and i != 0:
                    print(' - ', end='')
                elif koef[i] != 1:
                    print(koef[i], end='')
            else:
                if koef[i] == 1 and i != 0 and (i+1) != len(koef):
                    print(' +', end='')
                elif (i+1) != len(koef):
                    print(' +', koef[i], end='')
            if i == 1:
                print('x', end='')
            elif i > 1:
                print(f'xˇ{i}', end='')
   print()


def vlastnosti(koef):
    parne = []
    for i in koef:
        parne.append(i)
    for i in reversed(range(len(koef))):
        if i > 0 and i % 2 != 0:
            parne[i] = parne[i] * -1
    if parne == koef:
        print('Funkcia je párna')
    else:
        print('Funkcia nie je párna')
    for i in reversed(range(len(koef))):
        parne[i] = parne * -1
    if parne == koef:
        print('Funkcia je nepárna')
    else:
        print('Funkcia nie je nepárna')


#posun okna vlavo
def dolava(event):
   posun = abs(xmax.get() - xmin.get()) * 0.1
   xmax.set(xmax.get() - posun)
   xmin.set(xmin.get() - posun)
   vykreslenie_grafu()


#posun okna vpravo
def doprava(event):
   posun = abs(xmax.get() - xmin.get()) * 0.1
   xmax.set(xmax.get() + posun)
   xmin.set(xmin.get() + posun)
   vykreslenie_grafu()


#posun okna hore
def hore(event):
   posun = abs(ymax.get() - ymin.get()) * 0.1
   ymax.set(ymax.get() + posun)
   ymin.set(ymin.get() + posun)
   vykreslenie_grafu()


#posun okna dolu
def dolu(event):
   posun = abs(ymax.get() - ymin.get()) * 0.1
   ymax.set(ymax.get() - posun)
   ymin.set(ymin.get() - posun)
   vykreslenie_grafu()


def zvacsenie(event):
   xmax.set(xmax.get() * 0.9)
   xmin.set(xmin.get() * 0.9)
   ymax.set(ymax.get() * 0.9)
   ymin.set(ymin.get() * 0.9)
   zmaz()
   vykreslenie_grafu()


#zoom out
def zmensenie(event):
   xmax.set(xmax.get() * 10 / 9)
   xmin.set(xmin.get() * 10 / 9)
   ymax.set(ymax.get() * 10 / 9)
   ymin.set(ymin.get() * 10 / 9)
   zmaz()
   vykreslenie_grafu()


def vykreslenie_grafu():
   zmaz()
   x_min = int(xmin.get())
   x_max = int(xmax.get())
   y_min = int(ymin.get())
   y_max = int(ymax.get())

   #vykreslenie suradnicovych osi
     #pocet dielov na osi x
   pocetDielovX = abs(x_max - x_min)
     #pocet dielov na osi y
   pocetDielovY = abs(y_max - y_min)
     #x-ova suradnica priesecnika osi
   x0 = platno.winfo_width() / pocetDielovX * abs(x_min)
     #y-ova suradnica priesecnika osi
   y0 = platno.winfo_height() / pocetDielovY * abs(y_max)
     #os x-ova
   platno.create_line(x0, 0, x0, platno.winfo_height())
     #os y-ova
   platno.create_line(0, y0, platno.winfo_width(), y0)


   #vypocitame si rozdiel dvoch susednych grafickych bodov - jeho realnu hodnotu
   dx = (x_max - x_min) / platno.winfo_width()
   dy = (y_max - y_min) / platno.winfo_height()

   #vykreslenie grafu
   for t in range(0, platno.winfo_width() + 1):
       x = x_min + dx * t
       f = fx(koef, x)
       y = (y_max - f) / dy
       platno.create_oval(t - 1.5, y - 1.5, t + 1.5, y + 1.5, outline = 'red', fill = 'red')

   #vykreslenie grafu derivacie
   for t in range(0, platno.winfo_width() + 1):
       x = x_min + dx * t
       aa = derivacia(koef, 1)
       f = fx(aa, x)
       y = (y_max - f) / dy
       platno.create_oval(t - 1.5, y - 1.5, t + 1.5, y + 1.5, outline = 'blue', fill = 'blue')


def zmaz():
   platno.delete('all')


koef = []
volba = 0
while volba != 8:
   volba = menu()
   if volba == 1:
       koef = nacitaj_funkciu()
   elif volba == 2:
       fx(koef, 2)
   elif volba == 3:
       hladaj_korene()
   elif volba == 4:
       numericke(koef)
   elif volba == 5:
       derivacia(koef, 0)
   elif volba == 6:
       vlastnosti(koef)
   elif volba == 7:
       okno = tkinter.Tk()
       okno.title('Vykreslenie grafu funkcie')

       # globalne premenne programu
       platno = tkinter.Canvas(okno, width=800, height=400)
       platno.grid(row=4, column=0, columnspan=5)

       tkinter.Label(okno, text='xmin = ').grid(row=0, column=0, sticky='e')
       tkinter.Label(okno, text='xmax = ').grid(row=0, column=2, sticky='e')
       tkinter.Label(okno, text='ymin = ').grid(row=1, column=0, sticky='e')
       tkinter.Label(okno, text='ymax = ').grid(row=1, column=2, sticky='e')

       xmin = tkinter.DoubleVar()
       xmin.set(-5)
       tkinter.Entry(okno, textvariable=xmin).grid(row=0, column=1, sticky='w')
       xmax = tkinter.DoubleVar()
       xmax.set(5)
       tkinter.Entry(okno, textvariable=xmax).grid(row=0, column=3, sticky='w')
       ymin = tkinter.DoubleVar()
       ymin.set(-5)
       tkinter.Entry(okno, textvariable=ymin).grid(row=1, column=1, sticky='w')
       ymax = tkinter.DoubleVar()
       ymax.set(10)
       tkinter.Entry(okno, textvariable=ymax).grid(row=1, column=3, sticky='w')
       tkinter.Button(okno, text='Kresli  ', command=vykreslenie_grafu).grid(row=0, column=4, sticky='ewsn')
       tkinter.Button(okno, text='Zmaž  ', command=zmaz).grid(row=1, column=4, sticky='ewsn')
       tkinter.Button(text='Koniec', command=okno.destroy).grid(row=2, column=4, sticky='ewsn')

       tkinter.Label(okno,
                     text='Posun okna vpravo - pravá šípka, vľavo - ľavá šípka, hore - šípka hore, dolu - šípka dolu, lupa - pravý kláves ctrl (zväčšenie) / ľavý kláves ctrl (zmenšenie)').grid(
           row=5, column=0, columnspan=5)

       okno.bind('<Left>', dolava)  # posun okna dolava
       okno.bind('<Right>', doprava)  # posun okna doprava
       okno.bind('<Up>', hore)  # posun okna hore
       okno.bind('<Down>', dolu)  # posun okna dole
       okno.bind('<Control_R>', zvacsenie)  # ctrl pravé - zvacsenie lupy
       okno.bind('<Control_L>', zmensenie)  # ctrl ľavé - zmensenie lupy
       okno.mainloop()
print('Dovidenia nabuduce')
