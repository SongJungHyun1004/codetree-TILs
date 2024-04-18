import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize
a, b, n = map(int, input().split())
graph = [
    []
    for _ in range(1001)
]
for bus in range(1, n+1):
    fare, pn = map(int, input().split())
    pass_points = list(map(int, input().split()))
    pre = pass_points[0]
    for nxt in pass_points[1:]:
        graph[pre].append((nxt, bus, fare))
        pre = nxt

def dijkstra(src, dst):
    dist = [(INF, INF)]*1001
    dist[src] = (0, 0)
    pq = []
    heappush(pq, (0, 0, -1, src))
    while pq:
        now_d, now_t, now_bus, now = heappop(pq)
        for nxt, nxt_bus, nxt_d in graph[now]:
            add_fare = nxt_d if now_bus != nxt_bus else 0
            if dist[nxt][0] > now_d + add_fare or (dist[nxt][0] == now_d + add_fare and dist[nxt][1] > now_t + 1):
                dist[nxt] = (now_d+add_fare, now_t+1)
                heappush(pq, (now_d+add_fare, now_t+1, nxt_bus, nxt))
    return dist[dst]

mn_fare, mn_time = dijkstra(a, b)
if mn_fare == INF:
    print(-1, -1)
else:
    print(mn_fare, mn_time)