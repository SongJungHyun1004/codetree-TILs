import heapq
import sys

INT_MAX = sys.maxsize
MAX_M = 900

# 변수 선언 및 입력
n, a, b = tuple(map(int, input().split()))
brackets = [
    [" "] * (n + 1)
    for _ in range(n + 1)
]
for i in range(1, n + 1):
    brackets[i] = " " + input()

m = 0
node_num = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
graph = [[] for _ in range(MAX_M + 1)]
pq = []

dist = [0] * (MAX_M + 1)
ans = 0


def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


def make_graph():
    global m

    # 각 칸에 1부터 순서대로
    # 번호를 붙여줍니다. (그래프에서의 정점 번호)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            m += 1
            node_num[i][j] = m
    
    # 각 칸에 대해
    # 인접한 칸을 조사하여
    # 그래프를 완성합니다.
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    node1 = node_num[x][y]
                    node2 = node_num[nx][ny]
                    cost = a if brackets[x][y] == brackets[nx][ny] else b
                    graph[node1].append((node2, cost))


def dijkstra(k):
    # 그래프에 있는 모든 노드들에 대해
    # 초기값을 전부 아주 큰 값으로 설정
    for i in range(1, m + 1):
        dist[i] = INT_MAX

    # 시작위치에는 dist값을 0으로 설정
    dist[k] = 0

    # 우선순위 큐에 시작점을 넣어줍니다.
    # 거리가 가까운 곳이 먼저 나와야 하며
    # 해당 지점이 어디인지에 대한 정보도 필요하므로
    # (거리, 정점 번호) 형태로 넣어줘야 합니다.
    heapq.heappush(pq, (0, k))

    # O(|E|log|V|) 다익스트라 코드
    # 우선순위 큐에
    # 원소가 남아있다면 계속 진행해줍니다.
    while pq:
        # 가장 거리가 가까운 정보를 받아온 뒤, 원소를 제거해줍니다.
        min_dist, min_index = heapq.heappop(pq)

        # 우선순위 큐를 이용하면
        # 같은 정점의 원소가 
        # 여러 번 들어가는 문제가 발생할 수 있어
        # min_dist가 최신 dist[min_index]값과 다르다면
        # 계산할 필요 없이 패스해줍니다.
        if min_dist != dist[min_index]:
            continue

        # 최솟값에 해당하는 정점에 연결된 간선들을 보며
        # 시작점으로부터의 최단거리 값을 갱신해줍니다.
        for target_index, target_dist in graph[min_index]:
            # 현재 위치에서 연결된 간선으로 가는 것이 더 작다면
            new_dist = dist[min_index] + target_dist
            if dist[target_index] > new_dist:
                # 값을 갱신해주고, 우선순위 큐에 해당 정보를 넣어줍니다.
                dist[target_index] = new_dist
                heapq.heappush(pq, (new_dist, target_index))

   
# 각 칸을 정점으로 하는 
# 그래프를 만들어줍니다.
make_graph()

# 각 칸을 시작으로 하는 
# Dijkstra를 진행합니다.
for i in range(1, m + 1):
    dijkstra(i)

    # 각 도착지에 대한
    # 최단거리 값 중
    # 최댓값을 계속 갱신해줍니다.
    for j in range(1, m + 1):
        ans = max(ans, dist[j])

print(ans)