def f(n):
    if n > 0:
        print(n, end=" ")
        f(n-2)
        print(n, end=" ")


f(5)
print()
f(6)
print()
f(7)
print()
f(8)

# wynik: F, P, P, F