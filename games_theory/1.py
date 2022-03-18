def f(k1, k2, h=0):
    if (k1 + k2 < 77 and h == 2) or (k1 + k2 >= 77 and h < 2):
        return False
    elif k1 + k2 >= 77 and h == 2:
        return True
    else:
        return f(k1 + 1, k2, h + 1) or f(k1, k2 + 1, h + 1) or f(k1 * 2, k2, h + 1) or f(k1, k2 * 2, h + 1)


l = 7
for i in range(1, 70):
    if f(l, i):
        print(i)
