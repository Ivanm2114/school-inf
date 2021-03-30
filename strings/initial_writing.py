s = input()
n = s.find(' ')
name = s[:n]
n1 = s.rfind(" ")
surname = s[n1 + 1:]
father = s[n+1:n1]
print(f'{surname} {name[0]}. {father[0]}.')
