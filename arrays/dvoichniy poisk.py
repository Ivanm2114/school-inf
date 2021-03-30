x = int(input())
a = sorted([1, 2, 7, 5, 3, 9, 0])
l = 0
r = len(a)
while l < r - 1:
    c = (l + r) // 2
    if x < a[c]:
        r = c
    else:
        l = c
if a[l] == x:
    print(f"A[{l}]={x}")
else:
    print('Not found')
