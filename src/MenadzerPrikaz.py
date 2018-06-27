from src.PretragaPrikaz import pretragaPrikaz
from src.Menadzer import unosProjekcije
from src.Menadzer import dodavanjeProdavca
def menadzerPrikaz():
    print(22 * "-")
    print("")
    print("1. Pretraga projekcija")
    print("2. Unos nove projekcije")
    print("3. Brisanje projekcije")
    print("4. Izmjena projekcije")
    print("5. Dodavanje prodavca")
    print("6. Odjava")
    print(22 * "-")
    print("Unesite broj funkcije")
    menadzerNavigacija()


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
                pretragaPrikaz()
            elif unosFunkcije == 2:
                unosProjekcije()
            elif unosFunkcije == 3:
                print("Brisanje projekcije")
            elif unosFunkcije == 4:
                print("Izmjena projekcije")
            elif unosFunkcije == 5:
                dodavanjeProdavca()
            elif unosFunkcije == 6:
                quit()



