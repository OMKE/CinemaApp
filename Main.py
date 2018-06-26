from  Login import loginProvjera
from Views import  *


def start():
    korisnik = loginProvjera()


    # Provjera uloge
    if korisnik["uloga"] == "menadzer":
        menadzerPrikaz()
        menadzerNavigacija()
    elif korisnik["uloga"] == "prodavac":
        prodavacPrikaz()
        prodavacNavigacija()


start()