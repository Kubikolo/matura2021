class Gracz:
    def __init__(self, id, kraj, rok, miesiac, dzien):
        self.id = id
        self.kraj = kraj
        self.rok = rok
        self.miesiac = miesiac
        self.dzien = dzien


f = open(r"gracze.txt", "r")
gracze = f.readlines()
lepsi_gracze = []
for i in range(1, len(gracze)):
    lepsi_gracze.append(gracze[i][:-1])

lista_graczy = []
for i in lepsi_gracze:
    dane = i.split("\t")
    id = int(dane[0])
    kraj = dane[1]
    data = dane[2].split("-")
    rok = int(data[0])
    miesiac = int(data[1])
    dzien = int(data[2])
    lista_graczy.append(Gracz(id, kraj, rok, miesiac, dzien))

kraje = {}
for i in lista_graczy:
    if i.rok == 2018:
        if i.kraj not in kraje.keys():
            kraje[i.kraj] = 1
        else:
            kraje[i.kraj] += 1

for i in range(5):
    max_kraj = ("Kraj", 0)
    for j in kraje.keys():
        if kraje[j] > max_kraj[1]:
            max_kraj = (j, kraje[j])
    print(max_kraj)
    del kraje[max_kraj[0]]

