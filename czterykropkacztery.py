class Napis:
    def __init__(self):
        self.string = ""

    def parse(self, line):
        if "DOPISZ" in line:
            self.string += line[-1]
        elif "ZMIEN" in line:
            cs = list(self.string)
            cs[-1] = line[-1]
            self.string = "".join(cs)
        elif "USUN" in line:
            self.string = self.string[:-1]
        elif "PRZESUN" in line:
            id = self.string.index(line[-1])
            cs = list(self.string)
            char = chr(ord(cs[id]) + 1)
            if char == "[":
                cs[id] = "A"
            else:
                cs[id] = char
            self.string = "".join(cs)

n = Napis()
instrukcje = open(r"instrukcje.txt", "r")
lista = instrukcje.readlines()
poprawna_lista = []
for i in lista:
    poprawna_lista.append(i[:-1])
for i in poprawna_lista:
    n.parse(i)
print(n.string)
