n = int(input("Zadaj pocet hviezd: "))
tmp = 1

for i in reversed(range(1, n+1)):
    print(tmp * " ", end="")
    tmp+=1
    print(i * "*", end = "")
    print("")