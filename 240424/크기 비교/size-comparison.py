import sys
INF = sys.maxsize
n, m = map(int, input().split())
graph = [
    [0]*(n+1)
    for _ in range(n+1)
]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(1, n+1):
    print(n-(sum(graph[i])+sum([graph[j][i] for j in range(1, n+1)])+1))