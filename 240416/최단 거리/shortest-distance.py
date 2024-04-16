n, m = map(int, input().split())
dist = [
    list(map(int, input().split()))
    for _ in range(n)
]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for _ in range(m):
    a, b = map(int, input().split())
    print(dist[a-1][b-1])