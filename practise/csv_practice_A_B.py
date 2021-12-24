class TStudent:
    name = ''
    surname = ''
    russian = 0
    math = 0
    history = 0
    physics = 0
    sum_points = 0


students = []
marks = open('marks.csv').readlines()
for i in range(len(marks)):
    s = TStudent()
    data = marks[i].split(',')
    s.name = data[1]
    s.surname = data[0]
    s.russian = int(data[3])
    s.math = int(data[2])
    s.physics = int(data[4])
    s.history = int(data[5])
    s.sum_points = s.math + s.history + s.russian + s.physics
    students.append(s)

amt = len(students)
total_history = 0
total_maths = 0
total_russian = 0
total_physics = 0
max_res = 0
for el in students:
    total_physics += el.physics
    total_russian += el.russian
    total_maths += el.math
    total_history += el.history
    max_res = max(max_res, el.sum_points)
avg_history = total_history / amt
avg_maths = total_maths / amt
avg_russian = total_russian / amt
avg_physics = total_physics / amt
print('Физика', avg_physics, '\n', 'Русский', avg_russian, '\n', 'Математика', avg_maths, '\n', 'История', avg_history,
      '\n', "Максимальный результат", max_res)

print()
max_res_students = []
for el in students:
    if el.sum_points == max_res:
        max_res_students.append([el.surname, el.name])

max_res_students.sort(key=lambda x:x[0])
for el in max_res_students:
    print(*el)

print()

count = 0
for el in students:
    if 2 in [el.math, el.physics, el.russian, el.history]:
        count += 1
print('Кол-во двоечников', count)

print()

