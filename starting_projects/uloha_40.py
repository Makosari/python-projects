import math

max = int(input("Zadaj hornu hranicu intervalu: "))

for x in range(-5, max+ 1):
    Y1 = math.cos(x)
    print(f'Y = {Y1}')
    
    if math.sin(x) == 0:
        print(f'Nemozno vzpocitat 1/math.sin(x)')
        
    else:
        Y2 = 1/math.sin(x)
        print(f'Y = {Y2}')
    
    if x-4 < 0 or (x-4)**(1/2) == 0:
        print(f'Nemozno vzpocitat x/((x-4)**(1/2))')
    else:
        Y3 = x/((x-4)**(1/2))
        print(f'Y = {Y3}')
    print("")
