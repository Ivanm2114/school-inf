from math import cos, sin

EPS = 0.001
x = -10
delta = 2 * EPS
count = 3


def y(a):
    return a ** 3 + 2 * a ** 2 - 8 * a + 1 + 5 * sin(a) - 12 * cos(a)


while count > 0:
    while y(x) * y(x + delta) > 0:
        x += delta
    print(x + EPS)
    count -= 1
    x += delta
