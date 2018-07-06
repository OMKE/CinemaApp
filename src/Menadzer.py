import Podaci as Podaci
import MenadzerPrikaz
import Pretraga
import datetime



listaProjekcija = Podaci.ucitavanjeProjekcija()
listaFilmova = Podaci.ucitavanjeFilmova()


def provjeriDatum(datumProjekcije, sala, vrijeme, duzina):

    novaProjekcijaSat, novaProjekcijaMinut = vrijeme.split("-")

    novaProjekcijaPocetak =  datetime.timedelta(hours=int(novaProjekcijaSat), minutes=int(novaProjekcijaMinut))
    novaProjekcijaTrajanje = datetime.timedelta(minutes=duzina)

    novaProjekcijaKraj = novaProjekcijaPocetak + novaProjekcijaTrajanje


    datum = []
    for i in listaProjekcija:
        if i["datum"] == datumProjekcije:
            datum.append(i)


    nijeZauzeto = False

    for i in datum:
        trajanje = i["duzina"]
        pocetak = i["vrijemePocetka"]

        sat, minut = pocetak.split("-")

        pocetakProjekcije = datetime.timedelta(hours=int(sat), minutes=int(minut))
        trajanjeProjekcije = datetime.timedelta(minutes=int(trajanje))


        krajProjekcije = pocetakProjekcije + trajanjeProjekcije

        if novaProjekcijaKraj < pocetakProjekcije:
            nijeZauzeto = True
            break
        elif novaProjekcijaPocetak > krajProjekcije:
            nijeZauzeto = True
        elif novaProjekcijaPocetak < krajProjekcije:
            if sala != i["sala"]:
                nijeZauzeto = True
                break
            else:
                nijeZauzeto = False
                break
        else:
            if sala != i["sala"]:
                nijeZauzeto = True
                break
            else:
                nijeZauzeto = False


    return nijeZauzeto




def prepraviDatum(unosDatuma):
    noviDatumLista = []
    for i in unosDatuma:

        if i == "/" or i == " " or i == ".":
            noviDatumLista.append("-")
        else:
            noviDatumLista.append(i)
    prepravljenDatum = "".join(noviDatumLista)

    return prepravljenDatum
def prepraviVrijeme(vrijeme):
    novoVrijemeLista = []
    for i in vrijeme:

        if i == "/" or i == "." or i == "*" or i == ":":
            novoVrijemeLista.append("-")
        else:
            novoVrijemeLista.append(i)
    prepravljenoVrijeme = "".join(novoVrijemeLista)

    return prepravljenoVrijeme



def unosProjekcije():
    global listaFilmova
    global listaProjekcija
    print(25 * "-")
    print("     Unos projekcije     ")
    print(25 * "-")
    print("")
    zanrovi = Pretraga.dodavanjeZanrova()


    while True:
        unosId = input("Unesite ID projekcije: ")
        nadjenID = False

        for i in listaProjekcija:
            if i["id"] == unosId:
                print("ID je zauzet, unesite opet")
                nadjenID = True


        if nadjenID == False:
            break




    while True:
        try:
            unosDatuma = input("Unesite datum projekcije u formatu (dd-mm-yyyy): ")
            datum = prepraviDatum(unosDatuma)
            datetime.datetime.strptime(datum, '%d-%m-%Y')
            break
        except ValueError:
            print("Datum nije validan, pokusajte ponovo")


    while True:
        try:
            unosVremena1 = input("Unesite vrijeme projekcije u formatu (hh-mm): ")
            unosVremena = prepraviVrijeme(unosVremena1)
            datetime.datetime.strptime((unosVremena), "%H-%M")
            break
        except ValueError:
            print("Vrijeme nije validno, pokusajte ponovo")


    print("Unesite ID filma. Ako zelite da kreirate novi, unesite: 'da'")
    print("")
    Pretraga.prikazFilmova()
    unosFilma = input()

    nadjen = False

    for i in listaFilmova:
        if unosFilma == i["id"]:
            print("Izabrali ste film: " + i["naziv"])
            film = i["naziv"]
            while True:
                try:
                    unosDuzine = int(input("Unesite duzinu projekcije u minutama: "))
                    break
                except ValueError:
                    print("Unos strigova nije dozvoljen")

            while True:
                try:
                    unosCijene = int(input("Unesite cijenu u dinarima: "))
                    break
                except ValueError:
                    print("Unos stringova nije dozvoljen")



            print("Unesite redni broj sale: ")
            print("- Dostupne sale -")
            sale = Podaci.sale
            counter = 0
            for i in sale:
                counter += 1
                print(str(counter) + ". " + str(i))
            izabranaSala = False
            sala = ""
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

            if provjeriDatum(datum, sala, unosVremena, unosDuzine) == False:
                print("Sala sa unesenim datumom i vremenom je zauzeta")
                unosProjekcije()
            else:

                while True:
                    try:
                        unosUkupnihMjesta = int(input("Unesite broj ukupnih mjesta: "))
                        break
                    except ValueError:
                        print("Unos stringova nije dozvoljen")
                while True:
                    try:
                        unosSlobodnihMjesta = int(input("Unesite broj slobodnih mjesta: "))
                        if unosSlobodnihMjesta <= unosUkupnihMjesta:
                            break

                    except ValueError:
                        if unosSlobodnihMjesta > unosUkupnihMjesta:
                            print("Broj slobodnih mjesta ne moze biti veci od ukupnog")
                        else:
                            print("Unos stringova nije dozvoljen")

                novaProjekcija = [unosId, datum, unosVremena, unosDuzine, unosCijene, film,sala, unosSlobodnihMjesta, unosUkupnihMjesta]
                kreiranjeProjekcije(novaProjekcija)
                listaProjekcija = azuriraj()
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
            Pretraga.prikazZanrova()
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
            Pretraga.prikazZanrova()

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
        listaFilmova = azurirajFilmove()
        while True:
            try:
                unosDuzine = int(input("Unesite duzinu projekcije u minutama: "))
                break
            except ValueError:
                print("Unos stringova nije dozvoljen")
        while True:
            try:
                unosCijene = int(input("Unesite cijenu u dinarima: "))
                break
            except ValueError:
                print("Unos stringova nije dozvoljen")

        print("Unesite redni broj sale: ")
        print("- Dostupne sale -")

        counter = 0
        sale = Podaci.sale
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
                print("Greska")


        if provjeriDatum(datum, sala, unosVremena, unosDuzine) == False:
            print("Sala sa unesenim datumom i vremenom je zauzeta")
            unosProjekcije()
        else:

            while True:
                try:
                    unosUkupnihMjesta = int(input("Unesite broj ukupnih mjesta: "))
                    break
                except ValueError:
                    print("Unos stringova nije dozvoljen")
            while True:
                try:
                    unosSlobodnihMjesta = int(input("Unesite broj slobodnih mjesta: "))
                    if unosSlobodnihMjesta <= unosUkupnihMjesta:
                        break

                except ValueError:
                    if unosSlobodnihMjesta > unosUkupnihMjesta:
                        print("Broj slobodnih mjesta ne moze biti veci od ukupnog")
                    else:
                        print("Unos stringova nije dozvoljen")

            novaProjekcija = [unosId, datum, unosVremena, unosDuzine, unosCijene, unosNaziva, sala, unosSlobodnihMjesta, unosUkupnihMjesta]
            kreiranjeProjekcije(novaProjekcija)
            listaProjekcija = azuriraj()
            print("")
            print("Projekcija je kreirana")
            print("")
            MenadzerPrikaz.menadzerPrikaz()



    if nadjen == False:
        print("Ne postoji film sa unesenim ID-ijem, pokusajte ponovo")
        unosProjekcije()


def kreiranjeProjekcije(projekcija):
    with open("data/projekcije.txt", "a") as projekcije:
        projekcije.write("\n")
        for i in projekcija:
            projekcije.write(str(i) + ";")


def provjeraDuplikata(datum, vrijeme, sala):
    duplikat = False
    for i in listaProjekcija:

        trajanje = i["datum"] + i["vrijemePocetka"]




def kreiranjeFilma(film):
    with open("data/filmovi.txt", 'a') as pisanjeFilmovi:
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

    with open("data/korisnici.txt", "a") as korisnici:
        korisnici.write("\n")
        for i in korisnik:
            korisnici.write(str(i) + ";")
        print("")
    print("Uspjesno ste dodali novog prodavca")
    MenadzerPrikaz.menadzerPrikaz()


def prikazProjekcija():
    update = azuriraj()

    for i in update:
        print(
            "ID: "+ i["id"] + " - Film: " + i["film"] + "\n   Datum: " + i["datum"] + " - " + i["vrijemePocetka"] + "   Duzina: " + i[
                "duzina"] + "   Cijena: " + i["cijena"] + "   Sala: " + i["sala"] + "   Slobodno mjesta: " +
            i["slobodnoMjesta"])

    print("")

    return update




def izmjenaProjekcije():
    global listaProjekcija
    print(28 * "-")
    print("     Izmjena projekcije     ")
    print(28 * "-")
    update = prikazProjekcija()

    unosId = input("Unesite ID projekcije koju zelite izmjeniti: ")

    sacuvan = False

    if sacuvan == False:
        nadjenFilm = False
        for i in update:
            if unosId == i["id"]:
                print("Izabrali ste projekciju: " + i["film"])
                while True:
                    try:
                        unosDatuma = input("Unesite datum projekcije u formatu (dd-mm-yyyy): ")
                        datum = prepraviDatum(unosDatuma)
                        datetime.datetime.strptime(datum, '%d-%m-%Y')
                        break
                    except ValueError:
                        print("Datum nije validan, pokusajte ponovo")
                while True:
                    try:
                        unosVremena1 = input("Unesite vrijeme projekcije u formatu (hh-mm): ")
                        unosVremena = prepraviVrijeme(unosVremena1)
                        datetime.datetime.strptime((unosVremena), "%H-%M")
                        break
                    except ValueError:
                        print("Vrijeme nije validno, pokusajte ponovo")
                while True:
                    try:
                        unosDuzine = int(input("Unesite duzinu projekcije u minutama: "))
                        break
                    except ValueError:
                        print("Unos stringova nije dozvoljen")
                while True:
                    try:
                        unosCijene = int(input("Unesite cijenu projekcije u dinarima: "))
                        break
                    except ValueError:
                        print("Unos stringova nije dozvoljen")


                datum = prepraviDatum(unosDatuma)
                print("")
                Pretraga.prikazFilmova()
                print("")
                print("Unesite ID filma. ")
                unosFilma = input()
                for j in listaFilmova:
                    if unosFilma == j["id"]:
                        nadjenFilm = True
                        print("Izabran film: " + j["naziv"])
                        film = j["naziv"]

                        print("Unesite redni broj sale: ")
                        print("- Dostupne sale -")
                        sale = Podaci.sale
                        counter = 0
                        for k in sale:
                            counter += 1
                            print(str(counter) + ". " + str(k))
                        izabranaSala = False
                        while izabranaSala == False:
                            redniBrojSale = int(input()) - 1
                            if redniBrojSale >= 0 and redniBrojSale <= len(sale):
                                sala = sale[redniBrojSale]

                                izabranaSala = True
                            else:
                                print("Ne postoji sala sa unesenim rednim brojem, pokusajte ponovo")
                                izabranaSala = False

                        if provjeriDatum(datum, sala, unosVremena, unosDuzine) == False:
                            print("Sala sa unesenim datumom i vremenom je zauzeta")
                            izmjenaProjekcije()

                        else:

                            while True:
                                try:
                                    unosUkupnihMjesta = int(input("Unesite broj ukupnih mjesta: "))
                                    break
                                except ValueError:
                                    print("Unos stringova nije dozvoljen")
                            while True:
                                try:
                                    unosSlobodnihMjesta = int(input("Unesite broj slobodnih mjesta: "))
                                    if unosSlobodnihMjesta <= unosUkupnihMjesta:
                                        break

                                except ValueError:
                                    if unosSlobodnihMjesta > unosUkupnihMjesta:
                                        print("Broj slobodnih mjesta ne moze biti veci od ukupnog")
                                    else:
                                        print("Unos stringova nije dozvoljen")


                            i["datum"] = datum
                            i["vrijemePocetka"] = unosVremena
                            i["duzina"] = unosDuzine
                            i["cijena"] = unosCijene
                            i["film"] = film
                            i["sala"] = sala
                            i["slobodnoMjesta"] = unosSlobodnihMjesta
                            i["ukupnoMjesta"] = unosUkupnihMjesta
                            sacuvan = True

        if nadjenFilm == False:
            print("Ne postoji film sa unesenim ID-ijem, pokusajte ponovo")
            izmjenaProjekcije()

        if sacuvan:
            print("Projekcije izgledaju ovako: ")
            print("")
            saveProjekcije(update)
            listaProjekcija = azuriraj()
            print("Projekcija je uspjesno izmjenjena")
            MenadzerPrikaz.menadzerPrikaz()


def azurirajFilmove():
    zanrovi = Podaci.zanrovi
    listaFilmova = []
    with open("data/filmovi.txt", 'r') as filmoviFajl:

        prvaLinija = True

        for line in filmoviFajl:
            line = line.strip()
            if prvaLinija:

                const = line.split(";")
                prvaLinija = False
            else:

                oFilmu = line.split(";")
                try:
                    zanr = oFilmu[2].split("/")
                except IndexError:
                    pass

                film = dict(zip(const, oFilmu))
                film["zanr"] = zanr

                if zanr not in zanrovi:
                    zanrovi.append(zanr)
                listaFilmova.append(film)

        with open("data/zanrovi.txt", 'w') as zanroviFajl:
            for i in zanrovi:
                for j in i:
                    zanroviFajl.write(str(j + ";"))

    return listaFilmova

def azuriraj():
    listaProjekcija = []

    with open("data/projekcije.txt", 'r') as projekcijeFajl:

        prvaLinija = True

        for line in projekcijeFajl:
            line = line.strip()
            if prvaLinija:
                const = line.split(";")
                prvaLinija = False
            else:

                oProjekciji = line.split(";")

                projekcija = dict(zip(const, oProjekciji))

                listaProjekcija.append(projekcija)

    return listaProjekcija


def saveProjekcije(projekcije):
    with open("data/projekcije.txt", 'w') as projekcijeWrite:
        projekcijeWrite.write("id;datum;vrijemePocetka;duzina;cijena;film;sala;slobodnoMjesta;ukupnoMjesta")
        for i in projekcije:
            projekcijeWrite.write("\n")
            for j in i.values():
                projekcijeWrite.write(str(j) + ";")


def brisanjeProjekcija():
    global listaProjekcija
    print(28 * "-")
    print("     Brisanje projekcije     ")
    print(28 * "-")

    counter = 0
    projekcije = azuriraj()

    for j in projekcije:
        counter += 1
        print(
            str(counter) + " - ID: " + j["id"] + ", Film: " + j["film"] + "\n   Datum: " + j["datum"] + " - " + j[
                "vrijemePocetka"] + "   Duzina: " + j[
                "duzina"] + " min   Cijena: " + j["cijena"] + " RSD   Sala: " + j["sala"] + "   Slobodno mjesta: " +
            j["slobodnoMjesta"] + "   Ukupno mjesta: " +
            j["ukupnoMjesta"])


    print("")


    while True:
        try:
            unosID = int(input("Unesite redni broj projekcije koju zelite obrisati: "))
            break
        except ValueError:
            print("Unos stringova nije dozvoljen")
    nadjen = False
    counter = 0
    for i in projekcije:
        counter += 1
        if counter == unosID:
            print("Izabrali ste projekciju: " + i["film"] + " - Datum: " + i["datum"] + " - Vrijeme pocetka: " + i["vrijemePocetka"] + " - Sala: " + i["sala"])

            potvrda = input("Brisanje (da/ne): ")
            if potvrda.lower() == "da":
                projekcije.pop(unosID - 1)
                print("")
                saveProjekcije(projekcije)
                listaProjekcija = azuriraj()
                print("Projekcija je uspjesno obrisana")
                MenadzerPrikaz.menadzerPrikaz()
                nadjen = True
            elif potvrda == "ne":
                MenadzerPrikaz.menadzerPrikaz()
            else:
                MenadzerPrikaz.menadzerPrikaz()


    if nadjen == False:
        print("")
        print("Projekcija sa unesenim ID-jem ne postoji")
        brisanjeProjekcija()





