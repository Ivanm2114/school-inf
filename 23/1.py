def f(n, num_passed, plus1=False):
    if n > 30:
        return 0
    if n > 20 and (not num_passed):
        return 0
    if n == 20:
        num_passed = True
    elif n == 30:
        return 1
    if plus1:
        return f(n + 3, num_passed) + f(n * 2, num_passed)
    else:
        return f(n + 3, num_passed) + f(n * 2, num_passed) + f(n + 1, num_passed, True)


print(f(3, False))
