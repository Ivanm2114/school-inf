arr = list(map(int, input('Массив:\n').split()))
num = int(input('Что ищем:\n'))

found = []
for i in range(len(arr)):
    if arr[i] == num:
        found.append(f'A[{i + 1}] ={num}')

if found:
    print('Нашли: ' + ', '.join(found))
else:
    print('Ничего не нашли')
