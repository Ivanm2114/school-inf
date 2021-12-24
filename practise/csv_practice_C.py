class TFile:
    name = ''
    size = 0
    type = ''
    creation_date = ''
    date_of_last_change = ''
    access_level = ''


files = []
f = open('files.csv').readlines()
for el in f:
    data = el.split(',')
    s = TFile()
    s.name = data[0]
    s.size = int(data[1])
    s.type = data[2]
    s.creation_date = data[3]
    s.date_of_last_change = data[4]
    s.access_level = data[5]
    files.append(s)

d = {}
for el in files:
    if el.type not in d:
        d[el.type] = 1
    else:
        d[el.type] += 1

for el in d.items():
    print(el[0], el[1])

print()

biggest = list(reversed(sorted(files, key=lambda x: x.size)))[:10]
for el in biggest:
    print(el.name, el.size)

print()

locked = []
for el in files:
    if el.type == 'презентация' and el.access_level == 'ограничен' and '2012' in el.date_of_last_change:
        locked.append(el)
for el in sorted(locked, key=lambda x: x.name):
    print(el.name, el.type, el.access_level, el.date_of_last_change)

print()

vids = []
for el in files:
    if el.type == 'видео' and el.size > 102400 and int(el.creation_date[3:5]) >= 6 and '2011' in el.creation_date:
        vids.append(el)

vids.sort(reverse=True, key=lambda x: x.size)
for el in vids:
    print(el.name, el.type, el.size, el.creation_date)
