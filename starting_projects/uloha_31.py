n = int(input("Zadaj pocet hviezd: "))

for i in reversed(range(1, n+1)):
    print(i * "*", end = "")
    print("")