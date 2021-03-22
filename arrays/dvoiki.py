def check(num):
    i = 0
    while 2 ** i < num:
        i += 1
    return 2 ** i == num


arr = [3, 1, 3, 17, 8, 82, 1024, 21]

b = []

for el in arr:
    if check(el):
        b.append(el)

print(b)
