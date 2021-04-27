f = open('k7-94.txt')
s = f.readline()
f.close()
instance = 0
curLen, maxLen = 0, 0
for i in range(len(s)):
    if s[i] == 'C':
        if instance != 3:
            curLen = 1
        else:
            curLen += 1
        instance = 3
    elif s[i] == 'B' and instance > 1:
        instance = 2
        curLen += 1
    elif s[i] == 'A' and 3 > instance > 0:
        instance = 1
        curLen += 1
        maxLen = max(maxLen, curLen)
    else:
        curLen = 0
        instance = 0
print(maxLen)
