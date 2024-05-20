import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(x):
    global edge, node
    node += 1
    visited[x] = True
    for nx in graph[x]:
        edge += 1
        if not visited[nx]:
            dfs(nx)

cnt = 0
visited = [False]*(n+1)
for i in range(1, n+1):
    if not visited[i]:
        edge, node = 0, 0
        dfs(i)
        if edge//2 == node-1:
            cnt += 1

print(cnt)