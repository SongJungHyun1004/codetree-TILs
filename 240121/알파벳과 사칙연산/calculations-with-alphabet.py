expr = input()
alpha = []
for i in expr:
    if i.isalpha() and i not in alpha:
        alpha.append(i)
n = len(alpha)
num = []
mx = 0

def cal(num):
    result = num[0][1]
    op = ''
    for i in expr[1:]:
        if i.isalpha():
            v = 0
            for a, nn in num:
                if i == a:
                    v = nn
            if op == '-':
                result -= v
            elif op == '+':
                result += v
            elif op == '*':
                result *= v
        else:
            op = i
    return result

def choose(i):
    global mx
    if i == n:
        ans = cal(num)
        mx = max(mx, ans)
        return
    for nn in range(1, 5):
        num.append((alpha[i], nn))
        choose(i+1)
        num.pop()

choose(0)
print(mx)