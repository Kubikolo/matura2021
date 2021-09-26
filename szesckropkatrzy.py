class Gracz:
    def __init__(self, id, j):
        self.id = id
        self.jednostki = [j]

    def __eq__(self, other):
        return self.id == other

    def __repr__(self):
        return str(self.id)

    def __lt__(self, other):
        return self.id < other.id


f = open(r"jednostki.txt")
jednostki = f.readlines()

lepsze_jednostki = []
for i in jednostki:
    lepsze_jednostki.append(i[:-1])

lepsze_jednostki.pop(0)
lista_graczy = []
for i in lepsze_jednostki:
    jednostka = i.split("\t")
    if int(jednostka[1]) in lista_graczy:
        lista_graczy[lista_graczy.index(int(jednostka[1]))].jednostki.append(jednostka[2])
    else:
        lista_graczy.append(Gracz(int(jednostka[1]), jednostka[2]))

gracze_bez_art = []
for i in lista_graczy:
    if "artylerzysta" not in i.jednostki:
        gracze_bez_art.append(i)
gracze_bez_art.sort()
print(gracze_bez_art)