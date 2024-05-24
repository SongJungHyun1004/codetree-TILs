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

def find(x, uf):
    if x == uf[x]:
        return x
    uf[x] = find(uf[x], uf)
    return uf[x]

def union(i, j, uf):
    x = find(i, uf)
    y = find(j, uf)
    uf[x] = y

def isPossible(mid):
    uf = [i for i in range(n+1)]
    for i, j, s in edges:
        if s >= mid:
            union(i, j, uf)
        if find(a, uf) == find(b, uf):
            return True
    return False

def binary_search():
    left = 1
    right = 10**9
    mx = left
    while left <= right:
        mid = (left+right)//2
        if isPossible(mid):
            left = mid+1
            mx = max(mx, mid)
        else:
            right = mid-1
    return mx

print(binary_search())