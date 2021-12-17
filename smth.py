f = open('filename')

N = int(f.readline())

begin = -1001 * N

LEN = 10

s = [begin] * LEN

s[0] = 0

for i in range(N):
    a, b = map(int, f.readline().split())
    v = [a, b]
    t = [begin] * LEN

    for m in s:
        for k in v:
            r = m + k
            t[r % LEN] = max(t[r % LEN], r)
    s = t.copy()

print(s[8])
