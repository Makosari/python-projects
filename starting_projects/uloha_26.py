n = int(input("Zadaj n: "))
tmp = 0

for i in range(1, n+1):
    tmp += 1/i * (i+1)

print(tmp)