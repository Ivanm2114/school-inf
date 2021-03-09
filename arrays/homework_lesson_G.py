n = int(input())

arr = [int(input())]

count = 1
maximum = arr[0]
for i in range(n - 1):
    x = int(input())
    arr.append(x)
    if x > maximum:
        maximum = x
        count = 1
    elif x == maximum:
        count += 1


print(count)
maxNum = max(arr)
print(arr.count(maxNum))