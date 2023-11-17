n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))
mx = float('-inf')
for i in range(n):
    work = [0]*1000
    for j in range(n):
        if i == j:
            continue
        a, b = lst[j]
        for k in range(a, b):
            work[k] = 1
    mx = max(mx, sum(work))
print(mx)