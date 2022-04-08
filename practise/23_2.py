def f(n):
    if n > 96:
        return 0
    if n == 96:

        return 1
    return f(n + 3) + f(2 * n)


print(f(12))
