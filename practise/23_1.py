def F(n, f=False):
    if n == 15 and f:
        return 1
    if n > 15 or n == 14:
        return 0
    if n == 10:
        f = True
    return F(n + 1, f) + F(n + 2, f) + F(n * 3, f)


print(F(1))
