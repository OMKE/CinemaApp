import Menadzer
import ProdavacPrikaz
import Login
import datetime
import uuid
racun = []
ukupnoZaPlatiti = []
def prodajaKarti():
    print(28 * "-")
    print("     Prodaja karata     ")
    print(28 * "-")


    projekcije = Menadzer.prikazProjekcija()

    nadjen = False
    unosId = input("Unesite ID projekcije: ")

    for i in projekcije:
        if unosId == i["id"]:
            nadjen = True
            print("Izabrali ste projekciju: " + i["film"] + " - Datum: " + i["datum"] + " - Vrijeme pocetka: " + i[
                "vrijemePocetka"] + " - Sala: " + i["sala"])
            while True:
                try:
                    unosBroja = int(input("Unesite broj karata koliko zelite prodati: "))
                    break
                except ValueError:
                    print("Unos rijeci nije dozvoljen, pokusajte ponovo")

            if unosBroja > int(i["slobodnoMjesta"]):
                print("Uneseni broj karata je veci od broja slobodnog mjesta")
                prodajaKarti()
            else:
                ukupno = int(i["cijena"]) * unosBroja
                slobodnaMjesta = int(i["slobodnoMjesta"]) - unosBroja
                i["slobodnoMjesta"] = slobodnaMjesta
                print("Ukupno za platiti: " + str(ukupno) + " RSD")
                racun.append(i)

                saveRacun(unosBroja)
                ukupnoZaPlatiti.append(ukupno)
                racun.pop(0)
    if nadjen == False:
        print("Ne postoji projekcija sa unesenim ID-jem")
        ProdavacPrikaz.prodavacPrikaz()
    josProjekcija = input("Ako zelite jos projekcija unesite rijec - da: ")
    if josProjekcija.lower() == "da":
        prodajaKarti()
    else:
        Menadzer.saveProjekcije(projekcije)
        zapisiRacun()
        print("Racun je zapisan u bazu podataka")



    ProdavacPrikaz.prodavacPrikaz()

def sracunajUkupno():
    suma = 0
    for i in ukupnoZaPlatiti:
        suma += i
    return suma



def saveRacun(unosBroja):
    with open("data/racuni.txt", "a") as racuni:
        racuni.write("\n" + 30 * "-")

        racuni.write("\n      Racun")

        for i in racun:
            racuni.write("            \nProjekcija: " + str(i["film"]) + "\n    - Datum: " + str(
                i["datum"]) + "\n    - Vrijeme pocetka: " + str(i[
                                                                    "vrijemePocetka"]) + "\n    - Sala: " + str(i["sala"]))
            racuni.write("\nBroj karata: " + str(unosBroja))

def zapisiRacun():
    ukupno = sracunajUkupno()
    with open("data/racuni.txt", "a") as racuni:
        racuni.write("\n")
        for j in Login.ulogovaniKorisnik:
            racuni.write("\nIznos: " + str(ukupno) + " RSD")
            racuni.write("\nProdavac: " + str(j["ime"] + " " + str(j["prezime"])))
            racuni.write("\nDatum: " + str(datetime.datetime.now()))
            racuni.write("\nSifra racuna: " + str(uuid.uuid1())[:8])
            racuni.write("\n")
            racuni.write(30 * "-")
            racuni.write("\n")


