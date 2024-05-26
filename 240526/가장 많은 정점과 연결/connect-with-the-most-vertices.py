import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
costs = [0]+list(map(int, input().split()))
uf = [[i, 1, costs[i]] for i in range(n+1)]

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
        uf[y][2] = min(uf[y][2], uf[x][2])

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

edges = []
for i in range(1, n+1):
    p = find(i)
    edges.append((i, uf[p][1], uf[p][2]))
edges.sort(key=lambda x:(-x[1], x[2]))

cost = 0
biggest = edges[0]
for i in range(1, n):
    if find(biggest[0]) != find(i):
        union(biggest[0], i)
        cost += biggest[2] + uf[find(i)][2]

print('NO' if cost > k else cost)