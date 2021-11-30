import math

min = int(input("Zadaj spodnu hranicu intervalu: "))
max = int(input("Zadaj hornu hranicu intervalu: "))

for x in range(min, max+ 1):
    Y1 = math.cos(x)
    if 2*x == 0:
        print("Nemozno delit 0.")
    else:
        Y2 = 5/(2*x)
        print(f'Y = {Y2}')

    print(f'Y = {Y1}')
    
    if x == 2:
        print("Nemozno delit 0.")
    else:
        Y3 = 1/(x*2-4)
        print(f'Y = {Y3}')

    print("")