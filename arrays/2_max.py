n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
# С возможностью повторения
max1 = arr[0]
max2 = -1
for i in range(1, n):
    x = arr[i]
    if max1 <= x:
        max2 = max1
        max1 = x
    elif max2 <= x:
        max2 = x
print(max2)


# Без возможности повторения
max1 = arr[0]
max2 = -1
for i in range(1, n):
    x = arr[i]
    if max1 < x:
        max2 = max1
        max1 = x
    elif max2 < x != max1:
        max2 = x
print(max2)

# или так

print(list(sorted(list(set(arr))))[-2:])


