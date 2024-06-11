expr = input()
var = {}
index = {}
idx = 0
for s in expr:
    if s.isalpha() and s not in var:
        var[s] = 0
        index[idx] = s
        idx += 1
n = len(var)

def convert():
    stack = []
    result = ''
    for s in expr:
        if s.isalpha():
            result += s
        else:
            if stack:
                result += stack.pop()
                stack.append(s)
            else:
                stack.append(s)
    if stack:
        result += stack.pop()
    return result

def cal(a, b, op):
    if op == '-':
        return a-b
    elif op == '+':
        return a+b
    elif op == '*':
        return a*b
        
def calculate():
    stack = []
    for s in expr2:
        if s.isalpha():
            stack.append(var[s])
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(cal(a, b, s))
    return stack[0]

def choose(i):
    global mx
    if i == n:
        mx = max(mx, calculate())
        return
    for nn in range(1, 5):
        var[index[i]] = nn
        choose(i+1)
        var[index[i]] = 0

expr2 = convert()
mx = 0   
choose(0)
print(mx)