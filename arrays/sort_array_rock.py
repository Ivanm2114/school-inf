a = [3, 5, 17, 8, 0, 121, 47, 3]

n = len(a)
for i in range(n - 1):
    for j in range(1, n-i):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]

print(a)
