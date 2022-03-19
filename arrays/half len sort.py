arr = [5, 3, 4, 2, 1, 6, 3, 2]
a = sorted(arr[:4])
b = sorted(arr[4:], reverse=True)
print(a + b)
