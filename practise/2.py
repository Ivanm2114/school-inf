print('a b c r')
for a in range(2):
    for b in range(2):
        for c in range(2):
            print(a, b, c, bool(((not a) or b) and (not (a and b) or (not c))))
