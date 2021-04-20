fin = open('in1.txt')
summ = 0
count = 0
for line in fin.readlines():
    summ += int(line)
    count += 1
fout = open('out1.txt', 'w')
fout.write('Summ is ' + str(summ) + '\nCount is ' + str(count) + '\nAverage is ' + str(summ/count))
print(summ)
print(count)
fin.close()
fout.close()
