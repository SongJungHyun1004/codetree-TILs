n = int(input())
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))
mn = float('inf')
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = lst[i]
        x2, y2 = lst[j]
        dist = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        mn = min(mn, dist)
print(mn)