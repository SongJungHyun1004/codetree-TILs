n, m, k = map(int, input().split())
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
    x, y = map(int, input().split())
    union(x, y)

arr = list(map(int, input().split()))
pre = arr[0]
for nxt in arr[1:]:
    if find(pre) != find(nxt):
        print(0)
        exit(0)
print(1)