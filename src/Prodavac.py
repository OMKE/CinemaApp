from src.Menadzer import prikazProjekcija, saveProjekcije
import src.ProdavacPrikaz
import src.Login

def prodajaKarti():
    print(28 * "-")
    print("     Prodaja karata     ")
    print(28 * "-")


    projekcije = prikazProjekcija()

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
                with open("data/racuni.txt", "a") as racuni:
                    racuni.write("\n")
                    racuni.write(30*"-")
                    racuni.write("\n            Racun  \nProjekcija " + str(i["film"]) + "\n    - Datum: " + str(i["datum"]) + "\n    - Vrijeme pocetka: " + str(i[
                "vrijemePocetka"]) + "\n    - Sala: " + str(i["sala"]))
                    racuni.write("\nBroj karata: " + str(unosBroja))
                    racuni.write("\nIznos: " + str(ukupno) + " RSD")
                    for j in src.Login.ulogovaniKorisnik:
                        racuni.write("\nProdavac: " + str(j["ime"] + " " + str(j["prezime"])))
                    racuni.write("\n")
                    racuni.write(30 * "-")

    saveProjekcije(projekcije)

    if nadjen == False:
        print("Ne postoji projekcija sa unesenim ID-jem")
        src.ProdavacPrikaz.prodavacPrikaz()

    src.ProdavacPrikaz.prodavacPrikaz()



