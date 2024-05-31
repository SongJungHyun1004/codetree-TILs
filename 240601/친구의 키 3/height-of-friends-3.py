import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
order = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
pq = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heappush(pq, i)
for _ in range(n):
    if not pq:
        print(-1)
        exit(0)
    else:
        x = heappop(pq)
        order.append(x)
        for y in graph[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                heappush(pq, y)

print(*order)