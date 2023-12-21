s = input()
stack = []
for i in s:
    if i == '(':
        stack.append(i)
    elif stack and i == ')':
        stack.pop()
    else:
        print('No')
        exit(0)
print('No') if stack else print('Yes')