from heapq import heappush, heappop
import sys
INF = sys.maxsize
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [
    []
    for _ in range(n+1)
]
for _ in range(m):
    s, e, d = map(int, input().split())
    graph[e].append((s, d))
    graph[s].append((e, d))

def dijkstra(src):
    dist = [INF]*(n+1)
    dist[src] = 0
    pq = []
    heappush(pq, (0, src))
    while pq:
        now_d, now = heappop(pq)
        if dist[now] < now_d:
            continue
        for nxt, nxt_d in graph[now]:
            if dist[nxt] > now_d+nxt_d:
                dist[nxt] = now_d+nxt_d
                heappush(pq, (dist[nxt], nxt))
    return dist

dist = dijkstra(n)
dist.pop(0)
print(max(dist))