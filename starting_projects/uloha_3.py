polomer = float(input('Zadaj polomer: '))
vzdialenost = float(input('Zadaj vzdialenst od stredu kruznice: '))
vypocet = (((polomer**2) - (vzdialenost**2))**(1/2)) * 2
print(f'dlzka tetivy je: {vypocet}')