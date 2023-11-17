n = int(input())
lst = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    lst.append((x1, x2))
lst = sorted(lst)
stack = []
for l in lst:
    if stack:
        if stack[-1] < l[1]:
            stack.append(l[1])
            continue
        while stack and stack[-1] > l[1]:
            stack.pop()
    else:
        stack.append(l[1])
print(len(stack))