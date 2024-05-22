n = int(input())
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

for _ in range(n-2):
    s, e = map(int, input().split())
    union(s, e)

for i in range(2, n+1):
    if uf[i] != uf[1]:
        print(1, i)
        break