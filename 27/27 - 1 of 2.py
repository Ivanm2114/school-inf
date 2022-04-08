F = open("27_B.txt")
n = int(F.readline())
A = [int(x) for x in F.readlines()]
# n = 8
# A = [1, 11, 74, 2, 22, 122, 72, 1]
maxSumKr73 = 0
for i in range(0, n):
    curSum = 0
    for j in range(i, n):
        curSum += A[j]
        if curSum % 73 == 0 and curSum >= maxSumKr73:
            maxSumKr73 = curSum
            print(maxSumKr73, i, j)