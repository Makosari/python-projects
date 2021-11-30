a_x = int(input("Zadaj x-ovu suradnicu bodu A: "))
a_y = int(input("Zadaj y-ovu suradnicu bodu A: "))

b_x = int(input("Zadaj x-ovu suradnicu bodu B: "))
b_y = int(input("Zadaj y-ovu suradnicu bodu B: "))

c_x = int(input("Zadaj x-ovu suradnicu bodu C: "))
c_y = int(input("Zadaj y-ovu suradnicu bodu C: "))

a = (((b_x-c_x)**2)+((b_y - c_y)**2))**(1/2)
b = (((a_x-c_x)**2)+((a_y - c_y)**2))**(1/2)
c = (((a_x-b_x)**2)+((a_y - b_y)**2))**(1/2)

o = a+b+c
s = o/2 #polovicny obvod
S = (s*(s-a)*(s-b)*(s-c))**(1/2)

print(f'o = {o} \nS = {S}')