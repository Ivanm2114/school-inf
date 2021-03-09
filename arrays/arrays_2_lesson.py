n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

print(*arr)

maxNum = max(arr)

for i in range(n):
    if arr[i] == maxNum:
        print(f'A[{i}] = {maxNum}')

for i in range(n):
    if arr[i] == min(arr):
        print(f'A[{i}] = {min(arr)}')
