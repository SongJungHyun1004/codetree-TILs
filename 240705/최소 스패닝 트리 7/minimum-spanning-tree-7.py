import sys
sys.setrecursionlimit(40000)

import sys
import heapq

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

# mst를 위한 변수들
graph = [[] for _ in range(n + 1)]
pq = []
mst_edges = []

# Prim 진행시 각 노드가 MST에 연결되기 위해
# 어느 노드에 연결하는 것이 최선인지를 관리합니다.
dist_from = [0] * (n + 1)

# tree를 위한 변수들
edge = [[] for _ in range(n + 1)]
max_dist = 0
last_node = 0

dist = [0] * (n + 1)
visited = [False] * (n + 1)

# 그래프를 인접리스트로 표현합니다.
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x].append((y, z))
    graph[y].append((x, z))


def mst():
    # 그래프에 있는 모든 노드들에 대해
    # 초기값을 전부 아주 큰 값으로 설정
    for i in range(1, n + 1):
        dist[i] = INT_MAX

    # 시작위치에는 dist값을 0으로 설정
    dist[1] = 0

    # 우선순위 큐에 시작점을 넣어줍니다.
    # 거리가 가까운 곳이 먼저 나와야 하며
    # 해당 지점이 어디인지에 대한 정보도 필요하므로
    # (거리, 정점 번호) 형태로 넣어줘야 합니다.
    heapq.heappush(pq, (0, 1))

    # O(|E|log|V|) 프림 코드
    # 우선순위 큐에
    # 원소가 남아있다면 계속 진행해줍니다.
    total_dist = 0
    while pq:
        # 가장 거리가 가까운 정보를 받아온 뒤, 원소를 제거해줍니다.
        min_dist, min_index = heapq.heappop(pq)

        # 우선순위 큐를 이용하면
        # 같은 정점의 원소가 
        # 여러 번 들어가는 문제가 발생할 수 있어
        # 이미 계산해본 적이 있는 경우라면
        # 바로 패스해줍니다.
        if visited[min_index]:
            continue

        # visited 값을 true로 바꿔주고
        # 답을 갱신해줍니다. 
        visited[min_index] = True

        # mst에 해당하는 간선들을 만들어줍니다.
        if min_index != 1:
            mst_edges.append((
                min(min_index, dist_from[min_index]), 
                max(min_index, dist_from[min_index]), 
                dist[min_index]
            ))

        total_dist += min_dist

        # 최솟값에 해당하는 정점에 연결된 간선들을 보며
        # 최솟값을 갱신해줍니다.
        for target_index, target_dist in graph[min_index]:
            # 현재 위치에서 연결된 간선으로 가는 것이 더 작다면
            new_dist = target_dist
            if dist[target_index] > new_dist:
                # 값을 갱신해주고, 우선순위 큐에 해당 정보를 넣어줍니다.
                dist[target_index] = new_dist
                heapq.heappush(pq, (new_dist, target_index))

                # target_index번 정점이 새로 MST에 들어오기 위해서는 
                # min_index 정점과 연결되는 것이 최선임을 표시해줍니다.
                dist_from[target_index] = min_index

    return total_dist


# 모든 노드의 정점을 탐색하는 DFS를 진행합니다.
def dfs(x):
    global max_dist, last_node

    for y, d in edge[x]:
        # 이미 방문한 정점이면 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True
        dist[y] = dist[x] + d

        # 현재 정점을 기준으로 가장 먼 노드를 찾습니다.
        if dist[y] > max_dist:
            max_dist = dist[y]
            last_node = y

        dfs(y)


def tree_diameter():
    # n - 1개의 간선 정보를 인접리스트에 넣어줍니다.
    for x, y, d in mst_edges:
        edge[x].append((y, d))
        edge[y].append((x, d))
    
    # DFS를 통해 가장 먼 노드를 찾습니다.
    for i in range(1, n + 1):
        visited[i] = False
        dist[i] = 0

    visited[1] = True
    dfs(1)

    # 가장 먼 노드에서 시작해 다시 한번 DFS를 돌려 트리의 가장 긴 거리를 찾습니다.
    for i in range(1, n + 1):
        visited[i] = False
        dist[i] = 0

    visited[last_node] = True
    dfs(last_node)

    # 트리의 가장 긴 거리를 출력합니다.
    return max_dist


print(mst())
print(tree_diameter())