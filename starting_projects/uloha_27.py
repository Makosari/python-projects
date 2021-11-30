n = int(input("Zadaj n: "))
tmp = 0
tmp2 = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        tmp2 = tmp2*j
    tmp += 1/tmp2
    tmp2 = 1

print(tmp)
        