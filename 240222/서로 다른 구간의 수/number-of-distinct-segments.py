n = int(input())
lst = []
for i in range(n):
    a, b = map(int, input().split())
    lst.append((a, +1, i))
    lst.append((b, -1, i))
lst = sorted(lst)

group = []
cnt = 0
for nn, v, i in lst:
    if v == +1:
        if not group:
            cnt += 1
        group.append(i)
    else:
        group.remove(i)
print(cnt)