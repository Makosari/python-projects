n = int(input("Zadaj pocet hviezd: "))
tmp = n

if n%2 != 0:
    for i in range(1, n+1):
        print(tmp * " ", end="")
        tmp-=1
        print(i * "* ", end = "")
        print("")
else:
    print("Pocet znakov musi byt neparny")