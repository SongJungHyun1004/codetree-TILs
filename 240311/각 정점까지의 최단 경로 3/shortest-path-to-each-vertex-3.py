import heapq as hq
import sys
INF = sys.maxsize
n, m = map(int, input().split())
graph = [
    []
    for _ in range(n+1)
]
for _ in range(m):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))
dist = [INF]*(n+1)
dist[1] = 0
pq = []
for i in range(1, n+1):
    hq.heappush(pq, (dist[i], i))
while pq:
    now_d, now = hq.heappop(pq)
    if dist[now] < now_d:
        continue
    for nxt, nxt_d in graph[now]:
        if dist[nxt] > now_d + nxt_d:
            dist[nxt] = now_d + nxt_d
            hq.heappush(pq, (dist[nxt], nxt))

for i in range(2, n+1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])