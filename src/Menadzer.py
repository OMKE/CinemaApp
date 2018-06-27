from Podaci import *
from Pretraga import dodavanjeZanrova
from Pretraga import prikazFilmova
from Pretraga import prikazZanrova
import MenadzerPrikaz


listaProjekcija = ucitavanjeProjekcija()
listaFilmova = ucitavanjeFilmova()




def unosProjekcije():
    print(25 * "-")
    print("     Unos projekcije     ")
    print(25 * "-")
    print("")
    zanrovi = dodavanjeZanrova()
    IDs = []
    projekcije = ucitavanjeProjekcija()

    for i in projekcije:
        IDs.append(int(i["id"]))

    unosId = len(IDs) + 1


    unosDatuma = input("Unesite datum projekcije u formatu (dd.mm.yyyy): ")
    noviDatumLista = []
    for i in unosDatuma:

        if i == "/" or i == " " or i == "-":
            noviDatumLista.append(".")
        else:
            noviDatumLista.append(i)
    prepravljenDatum = "".join(noviDatumLista)

    unosVremena = input("Unesite vrijeme projekcije u formatu (hh:mm): ")

    print("Unesite ID filma. Ako zelite da kreirate novi, unesite: 'da'")
    print("")
    prikazFilmova()
    unosFilma = input()

    nadjen = False

    for i in listaFilmova:
        if unosFilma == i["id"]:
            print("Izabrali ste film: " + i["naziv"])
            film = i["naziv"]
            unosDuzine = input("Unesite duzinu projekcije u minutama: ")
            unosCijene = input("Unesite cijenu u dinarima: ")

            print("Unesite redni broj sale: ")
            print("- Dostupne sale -")

            counter = 0
            for i in sale:
                counter += 1
                print(str(counter) + ". " + str(i))
            izabranaSala = False
            while izabranaSala == False:
                try:
                    redniBrojSale = int(input()) - 1
                    if redniBrojSale >= 0 and redniBrojSale <= len(sale):
                        sala = sale[redniBrojSale]

                        izabranaSala = True
                    else:
                        print("Ne postoji sala sa unesenim rednim brojem, pokusajte ponovo")
                        izabranaSala = False
                except ValueError:
                    print(ValueError)
            nadjen = True

            if provjeraDuplikata(prepravljenDatum, unosVremena, sala):
                print("Sala sa unesenim datumom i vremenom je zauzeta")
                unosProjekcije()
            else:

                unosUkupnoMjesta = input("Unesite broj ukupnih mjesta: ")
                unosSlobodnihMjesta = input("Unesite broj slobodnih mjesta: ")
                novaProjekcija = [unosId, prepravljenDatum, unosVremena, unosDuzine, unosCijene, film,sala, unosSlobodnihMjesta, unosUkupnoMjesta]
                kreiranjeProjekcije(novaProjekcija)
                print("")
                print("Projekcija je kreirana")
                print("")
                MenadzerPrikaz.menadzerPrikaz()


    #         kreiranje novog filma
    if unosFilma.lower() == "da":
        idFilma = len(listaFilmova) + 1
        nadjen = True
        unosNaziva = input("Unesite naziv filma: ")

        netacanUnos = True
        while netacanUnos:
            prikazZanrova()
            print("Unesite redni broj zanra filma: ")

            try:
                unosZanra = int(input())
                unosZanra -= 1
                if unosZanra >= 0 and unosZanra <= len(zanrovi):
                    izabraniZanr1 = zanrovi[unosZanra]
                    netacanUnos = False
                else:
                    print("Unesite redni broj zanra od 1 do " + str(len(zanrovi)))
            except ValueError:
                print("Dozvoljen je unos samo brojeva")

        if netacanUnos == False:
            print("Unesite jos jedan zanr: ")
            prikazZanrova()

            netacanUnos = True
            while netacanUnos:

                try:
                    unosZanra = int(input())
                    unosZanra -= 1
                    if unosZanra >= 0 and unosZanra <= len(zanrovi):
                        izabraniZanr2 = zanrovi[unosZanra]
                        netacanUnos = False
                    else:
                        print("Unesite redni broj zanra od 1 do " + str(len(zanrovi)))
                except ValueError:
                    print("Dozvoljen je unos samo brojeva")

        noviFilm = [idFilma, unosNaziva,izabraniZanr1+ "/" + izabraniZanr2]
        kreiranjeFilma(noviFilm)
        unosDuzine = input("Unesite duzinu projekcije u minutama: ")
        unosCijene = input("Unesite cijenu u dinarima: ")

        print("Unesite redni broj sale: ")
        print("- Dostupne sale -")

        counter = 0
        for i in sale:
            counter += 1
            print(str(counter) + ". " + str(i))
        izabranaSala = False
        while izabranaSala == False:
            try:
                redniBrojSale = int(input()) - 1
                if redniBrojSale >= 0 and redniBrojSale <= len(sale):
                    sala = sale[redniBrojSale]

                    izabranaSala = True
                else:
                    print("Ne postoji sala sa unesenim rednim brojem, pokusajte ponovo")
                    izabranaSala = False
            except ValueError:
                print(ValueError)


        if provjeraDuplikata(prepravljenDatum, unosVremena, sala):
            print("Sala sa unesenim datumom i vremenom je zauzeta")
            unosProjekcije()
        else:

            unosUkupnoMjesta = input("Unesite broj ukupnih mjesta: ")
            unosSlobodnihMjesta = input("Unesite broj slobodnih mjesta: ")
            novaProjekcija = [unosId, prepravljenDatum, unosVremena, unosDuzine, unosCijene, unosNaziva, sala, unosSlobodnihMjesta, unosUkupnoMjesta]
            kreiranjeProjekcije(novaProjekcija)
            print("")
            print("Projekcija je kreirana")
            print("")
            MenadzerPrikaz.menadzerPrikaz()



    if nadjen == False:
        print("Ne postoji film sa unesenim ID-ijem, pokusajte ponovo")
        unosProjekcije()


def kreiranjeProjekcije(projekcija):
    with open("projekcije.txt", "a") as projekcije:
        projekcije.write("\n")
        for i in projekcija:
            projekcije.write(str(i) + ";")


def provjeraDuplikata(datum, vrijeme, sala):
    for i in listaProjekcija:
        if i["datum"] == datum and i["vrijemePocetka"] == vrijeme and i["sala"] == sala:
            return True
        else:
            return False


def kreiranjeFilma(film):
    with open("filmovi.txt", 'a') as pisanjeFilmovi:
        pisanjeFilmovi.write("\n")
        for i in film:

            pisanjeFilmovi.write(str(i) +  ";")



def dodavanjeProdavca():
    print(25 * "-")
    print("     Dodavanje prodavca     ")
    print(25 * "-")
    unosKorisnickogImena = input("Unesite korisnicko ime: ")
    unosLozinke = input("Unesite lozinku: ")
    unosImena = input("Unesite ime: ")
    unosPrezime = input("Unesite prezime: ")
    uloga = "prodavac"

    korisnik = [unosKorisnickogImena, unosLozinke, unosImena, unosPrezime, uloga]

    with open("korisnici.txt", "a") as korisnici:
        korisnici.write("\n")
        for i in korisnik:
            korisnici.write(str(i) + ";")
        print("")
    print("Uspjesno ste dodali novog prodavca")
    MenadzerPrikaz.menadzerPrikaz()



