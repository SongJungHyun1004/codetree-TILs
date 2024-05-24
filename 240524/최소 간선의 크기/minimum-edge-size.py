import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
INF = sys.maxsize
n, m = map(int, input().split())
a, b = map(int, input().split())
tree = [[] for i in range(n+1)]
for _ in range(m):
    i, j, s = map(int, input().split())
    tree[i].append((j, s))
    tree[j].append((i, s))

def dfs(x, mn):
    global mx
    visited[x] = True
    if x == b:
        mx = max(mx, mn)
    for nx, s in tree[x]:
        if not visited[nx]:
            dfs(nx, min(mn, s))
    visited[x] = False

visited = [False]*(n+1)
mx = 0
dfs(a, INF)
print(mx)