lists = input().split()
stack = []

for elem in lists:
    if elem == '+':
        a, b = stack.pop(), stack.pop()
        stack.append(b + a)
    elif elem == '-':
        a, b = stack.pop(), stack.pop()
        stack.append(b - a)
    elif elem == '*':
        a, b = stack.pop(), stack.pop()
        stack.append(b * a)
    elif elem == '/':
        a, b = stack.pop(), stack.pop()
        stack.append(b / a)
    else:
        stack.append(int(elem))

print(stack.pop())