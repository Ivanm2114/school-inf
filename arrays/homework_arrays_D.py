arr = list(map(int, input().split()))

i = 0
near = []
while i < len(arr) - 1:
    if arr[i] == arr[i+1] and arr[i] not in near:
        near.append(arr[i])
    i += 1
if near:
    print(*near)
else:
    print('Не нашли')