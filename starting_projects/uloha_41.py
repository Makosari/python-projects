import math

min = int(input("Zadaj dolnu hranicu intervalu: "))
max = int(input("Zadaj hornu hranicu intervalu: "))
krok = int(input("Zadaj krok: "))


for x in range(min, max+ 1, krok):
    if 5-x == 0:
        print("Nemozno vypocitat ((x**3)-2)/5-x")
    else:
        Y1 = ((x**3)-2)/5-x
        print(f'Y = {Y1}')
    

    if ((x**2)-1) == 0:
        print(f'Nemozno vzpocitat 2.1*x + 5/((x**2)-1)')
        
    else:
        Y2 = 2.1*x + 5/((x**2)-1)
        print(f'Y = {Y2}')
    

    if 4-(x**2) < 0 or (4-(x**2))**(1/2) == 0:
        print(f'Nemozno vzpocitat x/((4-(x**2))**(1/2))')
    else:
        Y3 = x/((4-(x**2))**(1/2))
        print(f'Y = {Y3}')
    print("")
