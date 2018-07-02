import src.PretragaPrikaz as PretragaPrikaz
import src.Menadzer as Menadzer


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
                PretragaPrikaz.pretragaPrikaz()
            elif unosFunkcije == 2:
                Menadzer.unosProjekcije()
            elif unosFunkcije == 3:
                Menadzer.brisanjeProjekcija()
            elif unosFunkcije == 4:
                Menadzer.izmjenaProjekcije()
            elif unosFunkcije == 5:
                Menadzer.dodavanjeProdavca()
            elif unosFunkcije == 6:
                quit()



