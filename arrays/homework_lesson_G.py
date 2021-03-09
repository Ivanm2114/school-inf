n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

maxNum = max(arr)
print(arr.count(maxNum))