n = int(input())
lst = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    lst.append((x1, x2))
cnt = 0
for i in range(n):
    flag = 0
    for j in range(n):
        if i == j:
            continue
        x1, x2 = lst[i]
        xx1, xx2 = lst[j]
        if not ((x1 < xx1 and x2 < xx2) or (x1 > xx1 and x2 > xx2)):
            flag = 1
    if not flag:
        cnt += 1
print(cnt)