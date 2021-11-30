x = int(input("Zadaj suradnicu x: "))
y = int(input("Zadaj suradnicu y: "))

if x > 0 and y > 0:
    print("I kvadrant")
elif x < 0 and y > 0:
    print("II kvadrant")
elif x < 0 and y < 0:
    print("III kvadrant")
else:
    print("IV kvadrant")