import string

instrukcje = open(r"instrukcje.txt", "r")
lista = instrukcje.readlines()
poprawna_lista = []
for i in lista:
    poprawna_lista.append(i[:-1])

d = dict.fromkeys(string.ascii_uppercase, 0)
for i in poprawna_lista:
    if i[0] == "D":
        d[i[-1]] += 1

letter = max(d, key=d.get)
print(letter)
print(d[letter])