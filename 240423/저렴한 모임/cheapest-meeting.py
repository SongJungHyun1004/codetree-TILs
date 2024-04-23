import sys
INF = sys.maxsize
n, m = map(int, input().split())
v1, v2, e = map(int, input().split())
graph = [
    [INF]*(n+1)
    for _ in range(n+1)
]
for i in range(1, n+1):
    graph[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

mn = INF
for meet in range(1, n+1):
    mn = min(mn, graph[v1][meet]+graph[v2][meet]+graph[meet][e])
print(mn if mn != INF else -1)