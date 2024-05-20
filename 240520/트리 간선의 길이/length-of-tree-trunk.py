n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e, d = map(int, input().split())
    tree[s].append((e, d))
    tree[e].append((s, d))

def dfs(x, dist):
    global ans
    ans = max(ans, dist)
    visited[x] = True
    for nx, nd in tree[x]:
        if not visited[nx]:
            dfs(nx, dist+nd)

ans = 0
for i in range(1, n+1):
    visited = [False]*(n+1)
    dfs(i, 0)
print(ans)