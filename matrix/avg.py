from random import randint

matrix = []
summa = 0
for i in range(4):
    matrix.append([])
    for j in range(4):
        a = randint(0, 255)
        summa += a
        matrix[i].append(a)

avg = summa / 16
print(*matrix, sep='\n')
for i in range(4):
    for j in range(4):
        if matrix[i][j] < avg:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 255

print(avg)
print(*matrix, sep='\n')
