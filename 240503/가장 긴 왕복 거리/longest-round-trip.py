import sys
input = sys.stdin.readline
from heapq import heappush, heappop
INF = sys.maxsize
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
    reverse_graph[e].append((s, d))

def dijkstra(src, graph):
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
    return dist[1:]

dist1 = dijkstra(x, graph)
dist2 = dijkstra(x, reverse_graph)
mx = 0
for d1, d2 in zip(dist1, dist2):
    mx = max(mx, d1+d2)
print(mx)