from math import cos

EPS = 0.001
x = 0
delta = 2 * EPS


def y(a):
    return a - cos(a)


while y(x) * y(x + delta) > 0:
    x += delta

print(x+EPS)

