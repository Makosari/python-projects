a_x = int(input("Zadaj x-ovu suradnicu bodu A: "))
a_y = int(input("Zadaj y-ovu suradnicu bodu A: "))

b_x = int(input("Zadaj x-ovu suradnicu bodu B: "))
b_y = int(input("Zadaj y-ovu suradnicu bodu B: "))

c_x = int(input("Zadaj x-ovu suradnicu bodu C: "))
c_y = int(input("Zadaj y-ovu suradnicu bodu C: "))

a = (((b_x-c_x)**2)+((b_y - c_y)**2))**(1/2)
b = (((a_x-c_x)**2)+((a_y - c_y)**2))**(1/2)
c = (((a_x-b_x)**2)+((a_y - b_y)**2))**(1/2)

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
