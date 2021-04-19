s = input()
i = 0
pos_strs = []
for el1 in ['A', 'C', 'E']:
    for el2 in ['A', 'D', 'F']:
        for el3 in ['A', 'B', 'F']:
            if el1 != el2 and el2 != el3:
                pos_strs.append(el1 + el2 + el3)
strings = []
for el in pos_strs:
    i = 0
    while i < len(s) - 2:
        if s[i:i + 3] == el and el not in strings:
            strings.append(el)
        i += 1
print(strings)
print(len(strings))
