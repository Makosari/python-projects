a = int(input('Zadaj stranu a: '))
b = int(input('Zadaj stranu b: '))
c = int(input('Zadaj stranu c: '))

list = []
list.append(a)
list.append(b)
list.append(c)
list.sort()
for i in range(len(list)):
    print(list[i], end = " ")

print()

list.sort(reverse=True)
for i in range(len(list)):
    print(list[i], end = " ")
