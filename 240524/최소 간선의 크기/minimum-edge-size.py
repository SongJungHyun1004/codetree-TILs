import sys
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
a, b = map(int, input().split())
edges = []
for _ in range(m):
    i, j, s = map(int, input().split())
    edges.append((i, j, s))
edges.sort(key=lambda x:-x[2])

def find(x):
    if x == uf[x]:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(i, j):
    x = find(i)
    y = find(j)
    uf[x] = y

uf = [i for i in range(n+1)]
for i, j, s in edges:
    union(i, j)
    if find(a) == find(b):
        print(s)
        break