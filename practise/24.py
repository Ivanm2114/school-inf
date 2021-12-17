f = open('24-3.txt').readline()
count = 1
max_count = 0
for i in range(len(f)-1):
    if f[i] < f[i+1]:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 1
print(max_count)