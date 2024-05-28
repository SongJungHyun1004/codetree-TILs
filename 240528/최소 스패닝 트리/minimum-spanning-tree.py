n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, d = map(int, input().split())
    edges.append((a, b, d))

edges.sort(key=lambda x:x[2])

def find(x):
    if x == uf[x]:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(a, b):
    x = find(a)
    y = find(b)
    uf[x] = y

uf = [i for i in range(n+1)]
cost = 0
for a, b, d in edges:
    if find(a) != find(b):
        union(a, b)
        cost += d
print(cost)