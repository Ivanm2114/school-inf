fin = open('in1.txt')
summ = 0
for line in fin.readlines():
    summ += int(line)
print(summ)