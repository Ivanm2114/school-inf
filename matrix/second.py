matr = []
n = int(input())
for i in range(n):
    matr.append([int(x) for x in input().split()])
summ = 0
for i in range(n):
    for j in range(len(matr[i])):
        if i == j:
            summ += matr[i][j]
print(summ)
for i in range(n):
    for j in range(len(matr[i])):
        if i >= j:
            summ += matr[i][j]
print(summ)
for i in range(n):
    for j in range(len(matr[i])):
        if i + j == n - 1:
            summ += matr[i][j]
print(summ)