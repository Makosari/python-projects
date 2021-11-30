a = float(input('Zadaj stranu a: '))
b = float(input('Zadaj stranu b: '))
c = float(input('Zadaj stranu c: '))
if  a + b > c and a - b < c:
    print("je mozne zostrojit trojuholnik")
else:
    print("Nie je mozne zostrojit trojuholnik")