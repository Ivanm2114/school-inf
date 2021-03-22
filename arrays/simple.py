def check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


arr = [3, 5, 3, 17, 8, 82, 100, 21]

b = []

for el in arr:
    if check(el):
        b.append(el)

print(b)
