n, m = map(int, input().split())
uf = [i for i in range(n+1)]

def find(x):
    if x == uf[x]:
        return x
    return find(uf[x])

def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        uf[x] = y
    else:
        uf[y] = x

cycle = set()
for _ in range(m):
    s, e = map(int, input().split())
    if find(s) != find(e):
        union(s, e)
    else:
        cycle.add(find(s))

uf = uf[1:]
tree = set()
for i in uf:
    if i not in cycle:
        tree.add(i)
print(len(tree))