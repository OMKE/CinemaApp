from src.PretragaPrikaz import pretragaPrikaz
from src.Prodavac import prodajaKarti
def prodavacPrikaz():
    print(22 * "-")
    print("")
    print("1. Pretraga projekcija")
    print("2. Prodaja karata")
    print("3. Odjava")
    print(22 * "-")
    print("Unesite broj funkcije")
    prodavacNavigacija()


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
                pretragaPrikaz()
            elif unosFunkcije == 2:
                prodajaKarti()
            elif unosFunkcije == 3:
                quit()
