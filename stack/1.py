import sys

stack = []
s = input()
pairs = {'}':'{', ']':'[', ')':'('}
for i in range(len(s)):
    if s[i] in '{[(':
        stack.append(s[i])
    elif s[i] in ']})':
        try:
            if pairs[s[i]] != stack.pop():
                print('Порядок скобок неверный')
                sys.exit(0)
        except IndexError:
            print('Количество открытых скобок не соответсвует количеству закрытых')
            sys.exit(0)


if len(stack) == 0:
    print('Все хорошо')
else:
    print("Количество открытых скобок не соответсвует количеству закрытых")