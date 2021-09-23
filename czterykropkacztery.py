class Napis:
    def __init__(self):
        self.string = ""

    def parse(self, line):
        if "DOPISZ" in line:
            self.string += line[-1]
        elif "ZMIEN" in line:
            siur = list(self.string)
            siur[-1] = line[-1]
            self.string = "".join(siur)
        elif "USUN" in line:
            self.string = self.string[:-1]
        elif "PRZESUN" in line:
            id = self.string.index(line[-1])
            siur = list(self.string)
            char = chr(ord(siur[id]) + 1)
            if char == "[":
                siur[id] = "A"
            else:
                siur[id] = char
            self.string = "".join(siur)

n = Napis()
instrukcje = open(r"instrukcje.txt", "r")
lista = instrukcje.readlines()
poprawna_lista = []
for i in lista:
    poprawna_lista.append(i[:-1])
for i in poprawna_lista:
    n.parse(i)
print(n.string)
