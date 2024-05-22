import sys
input = sys.stdin.readline

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

ans = -1
for i in range(1, m+1):
    s, e = map(int, input().split())
    if find(s) != find(e):
        union(s, e)
    else:
        ans = i
        break

print('happy' if ans == -1 else ans)