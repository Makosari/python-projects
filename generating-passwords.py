import random

#creates txt file named passwords.txt and generates random password (you can choose how many)

pocet = int(input('Enter number of passwords: '))
heslo = ''
b = 0
cislovanie = 1
subor = open('passwords.txt', 'w')
while b != pocet:
    for i in range(8):
        a = random.randint(64, 126)
        heslo += chr(a)
    subor.write(f'{cislovanie}. {heslo} \n')
    cislovanie += 1
    b += 1
    print(heslo)
    heslo = ''
