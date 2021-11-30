ph = int(input("Zadaj hodnotu pH: "))

if ph > 0 and ph <= 6:
    print("pH je kysle")
elif ph == 7:
    print("pH je neutralne")
elif ph > 7 and ph <= 14:
    print("pH je zasadite")
else:
    print("takato hodnota pH neexistuje")