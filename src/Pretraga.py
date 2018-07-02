import Podaci as Podaci
import Login as Login
import Menadzer as Menadzer


def pretragaPoID():
    listaProjekcija = Menadzer.azuriraj()

    unosId = input()

    nadjen = False
    for i in listaProjekcija:
        if i["id"] == unosId:
            print("Film: " + i["film"] + "\n   Datum: " + i["datum"] + " - " + i["vrijemePocetka"] + "\n   Duzina: " + i["duzina"] + "\n   Cijena: " + i["cijena"] + "\n   Sala: " + i["sala"] + "\n   Slobodno mjesta: " + i["slobodnoMjesta"])
            nadjen = True
            Login.redirect()
            break
    if nadjen == False:
        print("Ne postoji projekcija sa unesenim ID-jem")
        Login.redirect()




def pretragaPoNazivu():
    listaProjekcija = Menadzer.azuriraj()
    unosNaziva = input().lower()


    nadjen = False

    for i in listaProjekcija:
        nazivFilma = i["film"].lower()


        if unosNaziva in nazivFilma or unosNaziva == nazivFilma:
            print(
                "Film: " + i["film"] + "\n   Datum: " + i["datum"] + " - " + i["vrijemePocetka"] + "\n   Duzina: " + i[
                    "duzina"] + "\n   Cijena: " + i["cijena"] + "\n   Sala: " + i["sala"] + "\n   Slobodno mjesta: " +
                i["slobodnoMjesta"])
            nadjen = True



    if nadjen == False:
        print("Ne postoji projekcija sa unesenim nazivom")

    Login.redirect()


def dodavanjeZanrova():
    zanrovi = []
    with open("./data/zanrovi.txt", 'r') as zanroviFajl:
        for line in zanroviFajl:
            line = line.strip()
            zanroviLista = line.split(";")
            for i in zanroviLista:
                if i not  in zanrovi and i != "":
                    zanrovi.append(i)

    return zanrovi

def pretragaPoZanru():
    listaProjekcija = Menadzer.azuriraj()
    listaFilmova = Menadzer.azurirajFilmove()
    prikazZanrova()
    zanrovi = dodavanjeZanrova()

    netacanUnos = True
    while netacanUnos:
        try:
            unosZanra = int(input())
            netacanUnos = False
        except ValueError:
            netacanUnos = True
            print("Unos rijeci nije dozvoljen, pokusajte ponovo")

    if netacanUnos == False:
        unosZanra -= 1
        if unosZanra >= 0 and unosZanra <= len(zanrovi):
            print()
            print("Izabrali ste zanr: " + zanrovi[unosZanra])
            for i in listaFilmova:
                if zanrovi[unosZanra] in i["zanr"]:
                    for j in listaProjekcija:
                        if i["naziv"] == j["film"]:
                            print(
                                "Film: " + j["film"] + "\n   Datum: " + j["datum"] + " - " + j[
                                    "vrijemePocetka"] + "\n   Duzina: " + j[
                                    "duzina"] + "\n   Cijena: " + j["cijena"] + "\n   Sala: " + j[
                                    "sala"] + "\n   Slobodno mjesta: " +
                                j["slobodnoMjesta"])

    print("")
    Login.redirect()

def prikazFilmova():
    listaFilmova = Menadzer.azurirajFilmove()
    for i in listaFilmova:
        print("ID: " + i["id"] + " - "+ i["naziv"] + " - Zanr: " + ", ".join(i["zanr"]))

def prikazZanrova():
    counter = 0
    zanrovi = dodavanjeZanrova()

    for i in zanrovi:
        counter += 1
        print(str(counter) + " - " + i)

def pretragaPoSali():
    print("- Dostupne sale -")
    listaProjekcija = Menadzer.azuriraj()
    sale = Podaci.sale
    for i in sale:
        print(i + ", ", end="")


    print("")
    unosSale = input()
    unosSale.lower()
    nadjen = False
    for i in listaProjekcija:
        if i["sala"] == unosSale:
            print(
                "Film: " + i["film"] + "\n   Datum: " + i["datum"] + " - " + i["vrijemePocetka"] + "\n   Duzina: " + i[
                    "duzina"] + "\n   Cijena: " + i["cijena"] + "\n   Sala: " + i["sala"] + "\n   Slobodno mjesta: " +
                i["slobodnoMjesta"])
            nadjen = True
    if nadjen == False:
        print("Za navedenu salu nema predstojecih filmova")

    print("")
    Login.redirect()

