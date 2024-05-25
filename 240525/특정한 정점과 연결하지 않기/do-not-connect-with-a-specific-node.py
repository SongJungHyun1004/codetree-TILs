import sys
input = sys.stdin.readline

n, m = map(int, input().split())
uf = [[i, 1] for i in range(n+1)]

def find(x):
    if x == uf[x][0]:
        return x
    uf[x][0] = find(uf[x][0])
    return uf[x][0]

def union(a, b):
    x = find(a)
    y = find(b)
    if x != y:
        uf[x][0] = y
        uf[y][1] += uf[x][1]

for _ in range(m):
    i, j = map(int, input().split())
    union(i, j)

lst = []
for i in range(1, n+1):
    lst.append((i, uf[find(i)][1]))
lst.sort(key=lambda x:-x[1])

a, b, k = map(int, input().split())
for i, size in lst:
    if k == 0:
        break
    if find(i) != find(a) and find(i) != find(b):
        union(i, a)
        k -= 1
cnt = 0
for i in range(1, n+1):
    if find(a) == find(i):
        cnt += 1
print(cnt)