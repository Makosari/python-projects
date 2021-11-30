n = int(input("Zadaj cislo od 1 po 7: "))

if n < 1 or n > 7:
    print("Zle cislo")
else:
    if n >= 1 and n <= 5:
        print("Pracovny den")
    else:
        print("Volny den")