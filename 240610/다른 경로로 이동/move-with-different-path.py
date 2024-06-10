import sys
INF = sys.maxsize
from heapq import heappush, heappop

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
    graph[e].append((s, d))

def dijkstra(src, dst):
    dist = [INF]*(n+1)
    dist[src] = 0
    pq = []
    heappush(pq, (0, src))
    while pq:
        now_d, now = heappop(pq)
        if dist[now] < now_d:
            continue
        for nxt, nxt_d in graph[now]:
            if not visited[now][nxt] and dist[nxt] > now_d + nxt_d:
                dist[nxt] = now_d + nxt_d
                heappush(pq, (dist[nxt], nxt))
    return dist

dist = dijkstra(1, n)


def get_all_paths():
    paths = []
    stack = [(n, [n])]
    while stack:
        node, path = stack.pop()
        if node == 1:
            paths.append(path)
            continue
        for neighbor, weight in graph[node]:
            if dist[neighbor] == dist[node] - weight:
                stack.append((neighbor, [neighbor] + path))
    return paths

path = sorted(get_all_paths())[0]
for i in range(1, len(path)):
    frm, to = path[i-1], path[i]
    visited[frm][to] = True
    visited[to][frm] = True

dist = dijkstra(1, n)
print(-1 if dist[n] == INF else dist[n])