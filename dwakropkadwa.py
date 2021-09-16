def d(x, T):
	n = len(T)
	n += 1
	T.append(x)
	s = n
	while int(s/2) >= 1 and T[s - 1] > T[int(s/2) - 1]:
		pom = T[s - 1]
		T[s - 1] = T[int(s/2) - 1]
		T[int(s/2) - 1] = pom
		s = int(s/2)
	return T

tab = []
for i in [6, -4, 12, 27, 26, 8]:
	tab = d(i, tab)
print(tab)
