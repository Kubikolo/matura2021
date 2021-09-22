class Dzielnica:
    def __init__(self, nazwa, zuzycie):
        self.nazwa = nazwa
        self.zuzycie = zuzycie

    def __eq__(self, other):
        if type(other) == Dzielnica:
            return self.nazwa == other.nazwa
        else:
            return self.nazwa == other


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


def zlicz(tab1, tab2):
    for i in range(len(tab1)):
        tab1[i] += tab2[i]
    return tab1


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

lista_dzielnic = []
for i in lista_klientow:
    if i.kod_dzielnicy in lista_dzielnic:
        lista_dzielnic[lista_dzielnic.index(i.kod_dzielnicy)].zuzycie = zlicz(lista_dzielnic[lista_dzielnic.index(i.kod_dzielnicy)].zuzycie, i.zuzycie_wody)
    else:
        lista_dzielnic.append(Dzielnica(i.kod_dzielnicy, i.zuzycie_wody))

for dzielnica in lista_dzielnic:
    max_zuzycie = 0
    max_miesiac = 0
    for i in range(12):
        if dzielnica.zuzycie[i] > max_zuzycie:
            max_zuzycie = dzielnica.zuzycie[i]
            max_miesiac = i + 1
    print(dzielnica.nazwa, "w miesiącu", max_miesiac, "wartość:", max_zuzycie)
