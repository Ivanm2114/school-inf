s = input()
i = 0
maximum = 0
count = 0
for i in range(0, len(s) - 1):
    if s[i] == s[i + 1] == 'C':
        count += 1
    else:
        maximum = max(maximum, count + 1)
        count = 0
maximum = max(maximum, count + 1)
print(maximum)
