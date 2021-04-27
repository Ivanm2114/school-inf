f = open('k8-96.txt')
s = f.readline()
f.close()
curLen = 1
maxLen = 1
sym = ''
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        curLen += 1
    else:
        if curLen > maxLen:
            sym = s[i]
            maxLen = curLen
        curLen = 1
print(maxLen)
print(sym)
