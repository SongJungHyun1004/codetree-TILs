import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize
a, b, n = map(int, input().split())
graph = [
    [(INF, INF)]*1001
    for _ in range(1001)
]
for bus in range(1, n+1):
    fare, pn = map(int, input().split())
    pass_points = list(map(int, input().split()))
    for i in range(pn-1):
        for j in range(i, pn):
            x = pass_points[i]
            y = pass_points[j]
            graph[x][y] = min(graph[x][y], (fare, j-i))

def dijkstra(src, dst):
    dist = [(INF, INF)]*1001
    dist[src] = (0, 0)
    pq = []
    heappush(pq, (0, 0, src))
    while pq:
        now_d, now_t, now = heappop(pq)
        if dist[now] != (now_d, now_t):
            continue
        for i in range(1, 1001):
            nxt_dist = (graph[now][i][0]+now_d, graph[now][i][1]+now_t)
            if dist[i][0] > nxt_dist[0] or (dist[i][0] == nxt_dist[0] and dist[i][1] > nxt_dist[1]):
                dist[i] = nxt_dist
                heappush(pq, (nxt_dist[0], nxt_dist[1], i))
    return dist[dst]

mn_fare, mn_time = dijkstra(a, b)
if mn_fare == INF:
    print(-1, -1)
else:
    print(mn_fare, mn_time)