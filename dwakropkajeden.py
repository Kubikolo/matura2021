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

print(d(5, [26, 3, 5, -4]))
print(d(-5, [36, 15, 17, 3]))
print(d(30, [27, 6, 13, 4, -3, -2, -3]))
