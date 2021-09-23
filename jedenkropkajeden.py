import math

maxi = 0
mini = 10000
for i in range(1000, 8999):
    d = 9999 - i
    maxi = max(maxi, math.fabs(d - i))
    mini = min(mini, math.fabs(d - i))

print(maxi)
print(mini)