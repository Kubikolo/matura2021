instrukcje = open(r"przyklad.txt", "r")
lista = instrukcje.readlines()
poprawna_lista = []
for i in lista:
    poprawna_lista.append(i[:-1])

seria = ""
score = 1
highscore = 0
best_instruction = ""
for j in poprawna_lista:
    if seria == j[0]:
        score += 1
    else:
        score = 1
    highscore = max(highscore, score)
    seria = j[0]
print(highscore)