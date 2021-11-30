a = float(input('Zadaj stranu a: '))
b = float(input('Zadaj stranu b: '))
c = float(input('Zadaj stranu c: '))
if  a + b > c and a - b < c:
    if a == b and a == c and b == c:
        print("trojuholnik je rovnostranny")
    elif a == b and a != c and b != c:
        print("trojuholnik je rovnoramenny")
    elif a == c and a != b and b != c:
        print("trojuholnik je rovnoramenny")
    elif b == c and a != b and a != c:
        print("trojuholnik je rovnoramenny")
    else:
        print("Trojuholnik je roznostranny")
else:
    print("Nie je mozne zostrojit trojuholnik")