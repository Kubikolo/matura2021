def d_z_licznikiem(x, T):
	n = len(T)
	n += 1
	T.append(x)
	s = n
	global ile
	ile += 1
	while int(s/2) >= 1 and T[s - 1] > T[int(s/2) - 1]:
		pom = T[s - 1]
		T[s - 1] = T[int(s/2) - 1]
		T[int(s/2) - 1] = pom
		s = int(s/2)
		ile += 1
	return T


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

	
def zadanie(k):
	tab = []
	for i in range(1, k - 1):
		tab = 	d(i, tab)
	tab = d_z_licznikiem(k, tab)


ile = 0
zadanie(4)
print(ile)
ile = 0
zadanie(16)
print(ile)
ile = 0
zadanie(1025)
print(ile)
input()