import sys
from heapq import heappush, heappop

INF = sys.maxsize
n, m = map(int, input().split())
reds = list(map(int, input().split()))
blacks = [i+1 for i in range(n) if i+1 not in reds]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j, d = map(int, input().split())
    graph[i].append((j, d))
    graph[j].append((i, d))

memo = [[INF] * (n+1) for _ in range(n+1)]

def dijkstra(src, dst):
    if memo[src][dst] != INF:
        return memo[src][dst]
    dist = [INF]*(n+1)
    dist[src] = 0
    pq = []
    heappush(pq, (0, src))
    while pq:
        now_d, now = heappop(pq)
        if dist[now] < now_d:
            continue
        for nxt, nxt_d in graph[now]:
            if dist[nxt] > now_d + nxt_d:
                dist[nxt] = now_d + nxt_d
                heappush(pq, (dist[nxt], nxt))
    memo[src][dst] = dist[dst]
    return memo[src][dst]

mn = INF
for start in blacks:
    a = dijkstra(start, reds[0])
    b = dijkstra(reds[0], reds[1])
    c = dijkstra(reds[1], start)
    if a == INF or b == INF or c == INF:
        continue
    mn = min(mn, a+b+c)
print(mn if mn != INF else -1)