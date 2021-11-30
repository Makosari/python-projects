bod_x = int(input("Zadaj x-ovu suradnicu bodu: "))
bod_y = int(input("Zadaj y-ovu suradnicu bodu: "))

stred_x = int(input("Zadaj x-ovu suradnicu stredu kruznice: "))
stred_y = int(input("Zadaj y-ovu suradnicu stredu kruznice: "))

r = int(input("Zadaj polomer: "))

d = (((bod_x-stred_x)**2)+((bod_y - stred_y)**2))**(1/2)

if d < r:
    print("Bod sa nachadza v kruznici")
elif d > r:
    print("Bod sa nachadza mimo kruznice")
elif d == r:
    print("Bod sa nachadza na kruznici")
