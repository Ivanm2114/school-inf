from random import randint


def sumDig(x):
    summa = 0
    while x > 0:
        summa += x % 10
        x //= 10
    return summa


a = [randint(0, 5000) for x in range(10000)]
a.sort(key=sumDig)
print(a)