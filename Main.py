from  Login import loginProvjera
from MenadzerPrikaz import  *
from Views import prodavacNavigacija
from Views import prodavacPrikaz



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








