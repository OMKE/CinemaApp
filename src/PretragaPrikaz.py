from src.Pretraga import pretragaPoID, pretragaPoNazivu, pretragaPoZanru, pretragaPoSali




def pretragaPrikaz():
    print(18 * "-")
    print("     Pretraga     ")
    print(18 * "-")
    print("")
    print("1. Pretraga po ID-ju projekcije")
    print("2. Pretraga po nazivu filma")
    print("3. Pretraga po zanru filma")
    print("4. Pretraga po sali prikazivanja")
    print("")
    pretragaNavigacija()

def pretragaNavigacija():

    netacanUnos = True
    while netacanUnos:
        try:
            unosBroja = int(input("Unesite redni broj po kojem zelite pretrazivati: "))
            netacanUnos = False
        except ValueError:
            print("Unos rijeci nije dozvoljen, pokusajte ponovo")
            netacanUnos = True

        if netacanUnos == False:
            if unosBroja == 1:
                print("Unesite ID projekcije: ")
                pretragaPoID()
            elif unosBroja == 2:
                print("Unesite naziv filma: ")
                pretragaPoNazivu()
            elif unosBroja == 3:
                print("Unesite redni broj zanra filma: ")
                pretragaPoZanru()
            elif unosBroja == 4:
                print("Unesite redni broj sale: ")
                pretragaPoSali()
