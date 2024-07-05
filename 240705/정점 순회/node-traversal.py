import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n, s, d = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [0] * (n + 1)

ans = 0

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))

    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append(y)
    edges[y].append(x)


# DFS를 통해 연결된 모든 정점을 순회합니다.
# 동시에 dp값을 계산해줍니다.
def dfs(x):
    # 노드 x에 연결된 간선을 살펴보며 전부 방문해줍니다.
    for y in edges[x]:
        # 만약 y번 정점을 이미 방문했다면 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True
        dfs(y)

        # 가장 멀리 있는 리프노드까지의 거리를 저장합니다.
        dist[x] = max(dist[x], 1 + dist[y])


# 루트를 시작으로 DFS를 진행하며 값을 갱신합니다.
visited[s] = True
dfs(s)

# s번 정점을 제외한 리프까지의 거리가 d 이상인 정점의 개수를 구합니다.
for i in range(1, n + 1):
    if i == s: 
        continue
    if dist[i] >= d: 
        ans += 1

# s번 정점을 제외한 정답은 거리가 d이상인 정점의 개수 * 2가 됩니다.
print(ans * 2)