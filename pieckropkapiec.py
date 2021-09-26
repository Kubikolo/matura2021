from math import ceil
import matplotlib.pyplot as plt


class Klient:
    def __init__(self, numer_klienta, liczba_osob, kod_dzielnicy, zuzycie_wody):
        self.numer_klienta = numer_klienta
        self.liczba_osob = int(liczba_osob)
        self.kod_dzielnicy = kod_dzielnicy
        self.zuzycie_wody = zuzycie_wody
        self.suma = 0
        self.srednia = 0
        self.oblicz_sume()
        self.oblicz_srednia()

    def oblicz_sume(self):
        self.suma = 0
        for i in zuzycie_wody:
            self.suma += i

    def oblicz_srednia(self):
        self.srednia = self.suma/self.liczba_osob

    def __lt__(self, other):
        return self.srednia < other.srednia


def o_jeden_procent(wartosc, ilosc):
    for i in range(ilosc):
        wartosc *= 1.01
        wartosc = ceil(wartosc)
    return wartosc


f = open(r"wodociagi.txt", "r")
klienci = f.readlines()
lepsi_klienci = []
for i in klienci:
    lepsi_klienci.append(i[:-1])
lepsi_klienci.pop(0)
lista_klientow = []

for klient in lepsi_klienci:
    numer_klienta = klient[0:5]
    liczba_osob = klient[5:7]
    kod_dzielnicy = klient[7:10]
    zuzycie_wody = klient[11:].split(";")
    zuzycie_wody = [int(x) for x in zuzycie_wody]
    lista_klientow.append(Klient(numer_klienta, liczba_osob, kod_dzielnicy, zuzycie_wody))

miesiace = [0 for i in range(12)]
for i in lista_klientow:
    for j in range(12):
        miesiace[j] += i.zuzycie_wody[j]

przeplyw = 0
rok = 0
wynik_miesiac = 0
wynik_rok = 0
run = True
bonus = 0
while run:
    for i in range(12):
        przeplyw = o_jeden_procent(miesiace[i], rok)
        if przeplyw > 160000 + bonus:
            wynik_miesiac = i
            wynik_rok = rok
            run = False
            break
    rok += 1
    if rok + 2019 >= 2021:
        bonus += 1000

print("Rok:", 2019 + wynik_rok, "Miesiac:", wynik_miesiac + 1)
