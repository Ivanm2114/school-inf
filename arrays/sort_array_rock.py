from datetime import datetime
from random import randint

d1 = datetime.now()
a = [randint(0, 5000) for x in range(10000)]
b = a[:]
n = len(a)
for i in range(n - 1):
    for j in range(1, n - i):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
d2 = datetime.now()
print(a)
print(str(d2 - d1))
count = 0
c = b[:]
d3 = datetime.now()
for i in range(n - 1):
    nmin = i
    for j in range(i + 1, n):
        if b[j] < b[nmin]:
            nmin = j
            count += 1
    if b[i] != b[nmin]:
        b[i], b[nmin] = b[nmin], b[i]
d4 = datetime.now()
print(b)
print(count)
print(str(d4 - d3))
d5 = datetime.now()
c.sort()
d6 = datetime.now()
print(c)
print(str(d6 - d5))
