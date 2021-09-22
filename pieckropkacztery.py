from math import ceil

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
    for i in range(ilosc * 12):
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

styczen = 0
for i in lista_klientow:
    styczen += i.zuzycie_wody[4]
print(o_jeden_procent(styczen, 6))