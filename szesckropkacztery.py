from math import fabs


class Jednostka:
    def __init__(self, id, wlasciciel, nazwa, lok_x, lok_y):
        self.id = id
        self.wlasciciel = wlasciciel
        self.nazwa = nazwa
        self.lok_x = lok_x
        self.lok_y = lok_y


class Klasa:
    def __init__(self, nazwa, sila, strzal, magia, szybkosc):
        self.nazwa = nazwa
        self.sila = sila
        self.strzal = strzal
        self.magia = magia
        self.szybkosc = szybkosc


f1 = open(r"jednostki.txt", "r")
f2 = open(r"klasy.txt", "r")
jednostki = f1.readlines()
klasy = f2.readlines()

lepsze_jednostki = []
for i in jednostki:
    lepsze_jednostki.append(i[:-1])

lepsze_jednostki.pop(0)
lista_jednostek = []
for i in lepsze_jednostki:
    jednostka = i.split("\t")
    lista_jednostek.append(Jednostka(int(jednostka[0]), int(jednostka[1]), jednostka[2], int(jednostka[3]), int(jednostka[4])))

lepsze_klasy = []
for i in klasy:
    lepsze_klasy.append(i[:-1])

lepsze_klasy.pop(0)
lista_klas = []
for i in lepsze_klasy:
    klasa = i.split("\t")
    lista_klas.append(Klasa(klasa[0], int(klasa[1]), int(klasa[2]), int(klasa[3]), int(klasa[4])))

szybkosc = 0
d = {}
for i in lista_jednostek:
    for j in lista_klas:
        if i.nazwa == j.nazwa:
            szybkosc = j.szybkosc
    if fabs(i.lok_x - 100) + fabs(i.lok_y - 100) <= szybkosc:
        if i.nazwa in d.keys():
            d[i.nazwa] += 1
        else:
            d[i.nazwa] = 1
print(d)