n, m = map(int, input().split())
kind = ['']+list(input().split())
edges = []
for _ in range(m):
    i, j, d = map(int, input().split())
    edges.append((i, j, d))
edges.sort(key=lambda x:x[2])

uf = [i for i in range(n+1)]

def find(x):
    if x == uf[x]:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(i, j):
    x = find(i)
    y = find(j)
    uf[x] = y

cost = 0
for i, j, d in edges:
    if find(i) != find(j) and kind[i] != kind[j]:
        cost += d
        union(i, j)

first = find(1)
for i in range(2, n+1):
    if first != find(i):
        print(-1)
        exit(0)
print(cost)