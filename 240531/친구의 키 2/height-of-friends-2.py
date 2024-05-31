import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
order = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

for i in range(1, n+1):
    if not q:
        print('Inconsistent')
        exit(0)
    else:
        x = q.popleft()
        order.append(x)
        while graph[x]:
            y = graph[x].pop()
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)

print('Consistent')