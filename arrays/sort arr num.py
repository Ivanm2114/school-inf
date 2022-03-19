a = [332, 17, 332125, 1221, 4, 12318, 99, 773]
print(a)
a.sort(key=lambda x: len(str(x)), reverse=True)
print(a)
