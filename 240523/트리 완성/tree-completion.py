import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
uf = [i for i in range(n+1)]

def find(x):
    if x == uf[x]:
        return x
    return find(uf[x])

def union(a, b):
    x = find(a)
    y = find(b)
    if x != y:
        uf[x] = y

cut = 0
for _ in range(m):
    s, e = map(int, input().split())
    if find(s) != find(e):
        union(s, e)
    else:
        cut += 1

connect = 0
parents = [find(1)]
for i in range(2, n+1):
    if not find(i) in parents:
        parents.append(find(i))
        connect += 1

print(cut+connect)