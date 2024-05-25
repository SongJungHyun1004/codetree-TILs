import sys
input = sys.stdin.readline

n, m = map(int, input().split())
uf = [i for i in range(n+1)]

def find(x):
    if x == uf[x]:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(a, b):
    x = find(a)
    y = find(b)
    if x != y:
        uf[x] = y

for _ in range(m):
    i, j = map(int, input().split())
    union(i, j)

a, b, k = map(int, input().split())
for i in range(1, n+1):
    if k == 0:
        break
    if i == a:
        continue
    if find(i) != find(a) and find(i) != find(b):
        union(i, a)
        k -= 1
cnt = 0
for i in range(1, n+1):
    if find(a) == find(i):
        cnt += 1
print(cnt)