
def menadzerPrikaz():
    print(22 * "-")
    print("")
    print("1. Pretraga projekcija")
    print("2. Projekcije")
    print("3. Unos nove projekcije")
    print("4. Brisanje projekcije")
    print("5. Izmjena projekcije")
    print(22 * "-")
    print("Unesite broj funkcije")


def menadzerNavigacija():
    netacanInput = True
    while netacanInput:
        try:
            unosFunkcije = int(input())
            netacanInput = False

        except ValueError:
            print("Unos rijeci nije dozvoljen, pokusajte ponovo")
            netacanInput = True

        if netacanInput == False:
            if unosFunkcije == 1:
                print("Pretraga")
            elif unosFunkcije == 2:
                print("Projekcije")
            elif unosFunkcije == 3:
                print("Unos nove projekcije")
            elif unosFunkcije == 4:
                print("Brisanje projekcije")
            elif unosFunkcije == 5:
                print("Izmjena projekcije")




def prodavacPrikaz():
    print(22 * "-")
    print("Unesite broj funkcije")
    print("")
    print("1. Pretraga projekcija")
    print("2. Prodaja karata")
    print(22 * "-")
    print("Unesite broj funkcije")


def prodavacNavigacija():
    netacanInput = True
    while netacanInput:
        try:
            unosFunkcije = int(input())
            netacanInput = False

        except ValueError:
            print("Unos rijeci nije dozvoljen, pokusajte ponovo")
            netacanInput = True

        if netacanInput == False:
            if unosFunkcije == 1:
                print("Pretraga")
            elif unosFunkcije == 2:
                print("Prodaja karata")