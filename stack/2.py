stack = []
s = input().split()
for el in s:
    if el not in '+-*/^':
        stack.append(int(el))
    else:
        op2 = stack.pop()
        op1 = stack.pop()
        if el == '+':
            res = op2 + op1
        elif el == '-':
            res = op1 - op2
        elif el == '*':
            res = op2 * op1
        elif el == '/':
            res = op1 // op2
        elif el == '^':
            res = op1**op2
        stack.append(res)
print(stack[0])
