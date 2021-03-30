from datetime import datetime

arr = [0] * 100000000 + [1]

d1 = datetime.now()
count = 0
for i in range(len(arr)):
    if arr[i] == 1:
        count += 1
d2 = datetime.now()
print(count)
print(str(d2 - d1))
