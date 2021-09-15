def d(x):
	global n
	n += 1
	global T
	T.append(x)
	s = n
	while int(s/2) >= 1 and T[s - 1] > T[int(s/2) - 1]:
		pom  = T[s - 1]
		T[s - 1] = T[int(s/2) - 1]
		T[int(s/2) - 1] = pom
		s = int(s/2)

T = []
n = len(T)
d(6)
d(-4)
d(12)
d(27)
d(26)
d(8)
print(T)
breakpoint()
