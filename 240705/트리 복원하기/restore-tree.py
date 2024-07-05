import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

mst_edges = []

# 그래프에 있는 모든 노드들에 대해
# 초기값을 전부 아주 큰 값으로 설정
dist = [INT_MAX] * (n + 1) 

# Prim 진행시 각 노드가 MST에 연결되기 위해
# 어느 노드에 연결하는 것이 최선인지를 관리합니다.
dist_from = [0] * (n + 1)

# 그래프를 인접행렬을 입력받습니다.
for i in range(1, n + 1):
    row = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        graph[i][j] = row[j]

# 시작위치에는 dist값을 0으로 설정
dist[1] = 0

# O(|V|^2) 프림 코드
ans = 0
for i in range(1, n + 1):
    # V개의 정점 중 
    # 아직 방문하지 않은 정점 중
    # dist값이 가장 작은 정점을 찾아줍니다.
    min_index = -1
    for j in range(1, n + 1):
        if visited[j]:
            continue
        
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j

    # 최솟값에 해당하는 정점에 방문 표시를 진행합니다.
    visited[min_index] = True

    # mst에 해당하는 간선들을 저장합니다.
    if min_index != 1:
        mst_edges.append((
            min(min_index, dist_from[min_index]),
            max(min_index, dist_from[min_index]),
            dist[min_index]
        ))

    # mst 값을 갱신해줍니다.
    ans += dist[min_index]

    # 최솟값에 해당하는 정점에 연결된 간선들을 보며
    # 시작점으로부터의 최솟값을 갱신해줍니다.
    for j in range(1, n + 1):
        # 간선이 존재하지 않는 경우에는 넘어갑니다.
        if graph[min_index][j] == 0:
            continue

        # j번 노드로부터 가장 가까운 간선과
        # 그 간선의 정보들을 저장합니다.
        if dist[j] > graph[min_index][j]:
            dist[j] = graph[min_index][j]
            # j번 정점이 새로 MST에 들어오기 위해서는 
            # min_index 정점과 연결되는 것이 최선임을 표시해줍니다.
            dist_from[j] = min_index

# mst에 해당하는 간선들을 사전 순으로 정렬합니다.
mst_edges.sort()

for a, b, w in mst_edges:
    print(a, b, w)