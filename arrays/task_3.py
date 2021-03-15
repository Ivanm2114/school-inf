arr = list(map(int, input().split()))

repeat = []
for i in arr:
    x = arr.count(i)
    if x > 1 and i not in repeat:
        repeat.append(i)

if repeat:
    print(*repeat)
else:
    print('Не нашли')
