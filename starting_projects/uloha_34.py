n = int(input("Zadaj cislo od 1 po 7: "))

if n < 1 or n > 7:
    print("Zle cislo")
else:
    if n == 1:
        print("Pondelok")
    elif n == 2:
        print("Utorok")
    elif n == 3:
        print("Streda")
    elif n == 4:
        print("Stvrtok")
    elif n == 5:
        print("Piatok")
    elif n == 6:
        print("Sobota")
    elif n == 7:
        print("Nedela")
