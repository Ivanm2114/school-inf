arr = list(map(int, input().split()))

count = 1
maximum = arr[0]
for i in arr:
    if i > maximum:
        maximum = i
        count = 1
    elif i == maximum:
        count += 1

print("Значение", maximum)
print("Количество", count)
