import sys
import heapq

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
rev_a_graph = [[] for _ in range(n + 1)]
rev_b_graph = [[] for _ in range(n + 1)]
a_graph = [[] for _ in range(n + 1)]
b_graph = [[] for _ in range(n + 1)]
pq = []

dist = [0] * (n + 1)
a_dist = [0] * (n + 1)
b_dist = [0] * (n + 1)

# 그래프를 인접리스트로 표현합니다.
for _ in range(m):
    x, y, z1, z2 = tuple(map(int, input().split()))
    a_graph[x].append((y, z1))
    b_graph[x].append((y, z2))

    # 간선을 뒤집은 형태의 
    # 그래프도 미리 만들어둡니다.
    rev_a_graph[y].append((x, z1))
    rev_b_graph[y].append((x, z2))


# k를 시작점으로 하는 다익스트라 알고리즘을 진행합니다.
def dijkstra(k, dist, graph):
    # 그래프에 있는 모든 노드들에 대해
    # 초기값을 전부 아주 큰 값으로 설정
    for i in range(1, n + 1):
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


# 변형된 Dijkstra 알고리즘을 이용하여
# 최단거리를 계산합니다.
def modified_dijkstra(dist, a_dist, b_dist, a_graph, b_graph):
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
        length = len(a_graph[min_index])
        for j in range(length):
            target_index, a_cost = a_graph[min_index][j]
            target_index, b_cost = b_graph[min_index][j]
            
            # 그림 A, B에 대해
            # 최단거리에 맞는 간선이 아닌 경우
            # 경고 횟수를 1씩 세줍니다.
            target_dist = 0
            if a_dist[target_index] + a_cost != a_dist[min_index]:
                target_dist += 1
            if b_dist[target_index] + b_cost != b_dist[min_index]:
                target_dist += 1

            # 현재 위치에서 연결된 간선으로 가는 것이 더 작다면
            new_dist = dist[min_index] + target_dist
            if dist[target_index] > new_dist:
                # 값을 갱신해주고, 우선순위 큐에 해당 정보를 넣어줍니다.
                dist[target_index] = new_dist
                heapq.heappush(pq, (new_dist, target_index))


# 그래프 간선 방향을 거꾸로 뒤집은 그래프에 대해
# n번 정점을 시작으로 하는 다익스트라를
# A번 그래프, B번 그래프에 대해 각각 1번씩 수행합니다.
dijkstra(n, a_dist, rev_a_graph)
dijkstra(n, b_dist, rev_b_graph)

# 처음 주어진 그래프 방향대로 그대로 이용하되
# 그래프 간선의 가중치의 경우
# 그림 A, B에 대해
# 최단거리가 아닌 횟수로
# 0, 1, 2 중 하나로 계산하여 
# 변형된 Dijkstra 알고리즘을 이용하여
# 최종 최단거리를 계산합니다.
modified_dijkstra(dist, a_dist, b_dist, a_graph, b_graph)

ans = dist[n]
print(ans)