N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
print(a)
print(*a)

summ = 0
for i in range(N):
    summ += a[i]

print(summ / N)

print(sum(a) / len(a))

summ2 = 0
count1 = 0
for maksimka in a:
    if maksimka >= 0:
        summ2 += maksimka
        count1 += 1

print(summ2 / count1)
