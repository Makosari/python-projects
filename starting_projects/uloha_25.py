n = int(input("Zadaj n: "))
tmp = 0

for i in range(1, n+1):
    if n%i == 0:
        tmp += 1
if tmp > 2:
    print("Cislo nie je prvocislo.")
else:
    print("Cislo je prvocislo.")