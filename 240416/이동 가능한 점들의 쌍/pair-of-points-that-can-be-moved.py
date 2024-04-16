import sys
input = sys.stdin.readline
MAX = sys.maxsize
n, m, p, q = map(int, input().split())

dist = [
    [MAX+1]*(n+1)
    for _ in range(n+1)
]
for i in range(1, n+1):
    dist[i][i] = 0
for _ in range(m):
    s, e, cost = map(int, input().split())
    dist[s][e] = cost

red = [i+1 for i in range(p)]

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])


cnt, total = 0, 0
for _ in range(q):
    s, e = map(int, input().split())
    mn = MAX
    for i in range(1, p+1):
        mn = min(mn, dist[s][i]+dist[i][e])
    if mn == MAX:
        continue
    cnt += 1
    total += mn
print(cnt)
print(total)