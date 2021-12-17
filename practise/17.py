arr = list(map(int, open('17-4.txt').readlines()))
avg = sum(arr) / len(arr)
count = 0
min_s = 20000000000
for i in range(0, len(arr) - 1):
    if (arr[i] < avg or arr[i + 1] < avg) and '4' not in str(arr[i]) and '4' not in str(arr[i + 1]):
        count += 1
        if arr[i] + arr[i + 1] < min_s:
            min_s = arr[i] + arr[i + 1]
print(count, min_s)
