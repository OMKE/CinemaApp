zanrovi = []
sale = ["1A","2A","3A","4A","5A","1B","2B","3B","4B","1C","2C","3C"]

def ucitavanjeFilmova():
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

def ucitavanjeProjekcija():
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











