import sys
INF = sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())
dist = [
    [INF]*(n+1)
    for _ in range(n+1)
]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    s, e, d = map(int, input().split())
    dist[s][e] = d

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

mn = INF
for s in range(1, n+1):
    for e in range(1, n+1):
        if s == e:
            continue
        if dist[s][e] == INF or dist[e][s] == INF:
            continue
        mn = min(mn, dist[s][e]+dist[e][s])
print(mn)