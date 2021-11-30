n = int(input("Zadaj pocet hviezd: "))
tmp = n

for i in range(1, n+1):
    print(tmp * " ", end="")
    tmp-=1
    print(i * "*", end = "")
    print("")