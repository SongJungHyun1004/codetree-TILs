n, m = map(int, input().split())
uf = [i for i in range(n+1)]

def find(x):
    if x == uf[x]:
        return x
    root = find(uf[x])
    uf[x] = root
    return root

def union(a, b):
    X = find(a)
    Y = find(b)
    if X != Y:
        uf[X] = Y

for _ in range(m):
    x, a, b = map(int, input().split())
    if x:
        if find(a) == find(b):
            print(1)
        else:
            print(0)
    else:
        union(a, b)