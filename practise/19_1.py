def F(n, h=0):
    if (h == 2 or h == 4) and n >= 22:
        return True
    if n >= 22 or (h > 4):
        return False
    if h % 2 == 0:
        if n % 2 == 1:
            return F(n + 1, h + 1) and F(n + 2, h + 1) and F(n * 2, h + 1)
        return F(n + 1, h + 1) and F(n + 2, h + 1)
    else:
        if n % 2 == 1:
            return F(n + 1, h + 1) or F(n + 2, h + 1) or F(n * 2, h + 1)
        return F(n + 1, h + 1) or F(n + 2, h + 1)


for i in range(1, 22):
    if F(i):
        print(i)
