import MenadzerPrikaz
import ProdavacPrikaz

ulogovaniKorisnik = []

def ucitavanjeKorisnika():
    listaKorisnika = []
    with open("data/korisnici.txt",'r') as korisniciFajl:

        prvaLinija = True

        for line in korisniciFajl:

            if prvaLinija:
                line = line.strip()
                const = line.split(";")
                prvaLinija = False
            else:
                line = line.strip()

                korisnikPodaci = line.split(";")

                korisnik = dict(zip(const, korisnikPodaci))
                listaKorisnika.append(korisnik)

        return listaKorisnika




def loginProvjera():
    listaKorisnika = ucitavanjeKorisnika()

    print("CinemaAPP")
    print(16 * "-")
    print("-    Login    -")
    print(16 * "-")
    print("")

    logginIn = True
    loggedIn = False
    while logginIn:
        try:
            unosKorisnickoIme = input("Unesite korisnicko ime: ")
            unosLozinka = input("Unesite lozinku: ")

            for i in listaKorisnika:
                if i["korisnickoIme"] == unosKorisnickoIme and i["lozinka"] == unosLozinka:
                    loggedIn = True
                    logginIn = False
                    ulogovaniKorisnik.append(i)
                    print("Dobrodosli " + i["ime"] + " - Uloga: " + i["uloga"])
                    redirect()
                    return i

            if loggedIn == False:
                logginIn = True
                print("")
                print("Pogresno korisnicko ime ili lozinka")
                print("")

        except ValueError:
            print(ValueError)




def redirect():
    if meni() == True:
        MenadzerPrikaz.menadzerPrikaz()
        MenadzerPrikaz.menadzerNavigacija()
    else:
        ProdavacPrikaz.prodavacPrikaz()
        ProdavacPrikaz.prodavacNavigacija()

def meni():
    for i in ulogovaniKorisnik:
        if i["uloga"] == "menadzer":
            return True
        elif i["uloga"] == "prodavac":
            return False