F = open("27_B.txt")
n = int(F.readline())
golovy = [0]*73
koncy_golov = [-1]*73
curSum = 0
maxSumKr73 = 0
minDlinaMaxKr73 = 0
for i in range(n):
    cislo = int(F.readline())
    curSum += cislo
    ostat = curSum % 73
    if golovy[ostat] == 0 and ostat != 0: 
        golovy[ostat] = curSum
        koncy_golov[ostat] = i
    else:
        if curSum - golovy[ostat] > maxSumKr73:
            maxSumKr73 = curSum - golovy[ostat]
            minDlinaMaxKr73 = i - koncy_golov[ostat]
        if curSum - golovy[ostat] == maxSumKr73:            
            if i - koncy_golov[ostat] < minDlinaMaxKr73:
                minDlinaMaxKr73 = i - koncy_golov[ostat]
print(maxSumKr73)
print(minDlinaMaxKr73)
    