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

dzielnice = {}
for i in lista_klientow:
    if i.kod_dzielnicy in dzielnice.keys():
        dzielnice[i.kod_dzielnicy] += i.suma
    else:
        dzielnice[i.kod_dzielnicy] = i.suma

print(dzielnice)