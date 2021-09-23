import math

liczba = int(input())
il_cyfr = math.floor(math.log10(liczba)) + 1
dziewiatki = pow(10, il_cyfr) - 1
dopelnienie = dziewiatki - liczba
print(dopelnienie)
