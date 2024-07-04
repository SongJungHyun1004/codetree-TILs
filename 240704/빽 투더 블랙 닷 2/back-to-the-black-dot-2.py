import sys
import heapq

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
a, b = tuple(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
pq = []

# 그래프에 있는 모든 노드들에 대해
# 초기값을 전부 아주 큰 값으로 설정
red_dist1 = [INT_MAX] * (n + 1)
red_dist2 = [INT_MAX] * (n + 1)

ans = INT_MAX

# 그래프를 인접리스트로 표현합니다.
# 양방향 그래프이므로
# 양쪽에 추가해줘야함에 유의합니다.
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x].append((y, z))
    graph[y].append((x, z))


# k를 시작점으로 하는 다익스트라 알고리즘을 진행합니다.
def dijkstra(k, dist):
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


# 시작점을 a, b로 하는 다익스트라를 각각 1번씩 수행합니다.
dijkstra(a, red_dist1)
dijkstra(b, red_dist2)

# 각 시작점 x에 대해
# 검정점 x -> 빨간점 1, 2 -> 검정점 x
# 순서로 이동하는 최단거리의 합 중
# 최솟값을 찾습니다.
for i in range(1, n + 1):
    # i가 검정점이 아니라면
    # 패스합니다.
    if i == a or i == b:
        continue

    # 검정점 i -> 빨간점 1 -> 빨간점 2 -> 검정점 i
    # 순으로 돌아오는 경우입니다.
    ans = min(ans, red_dist1[i] + red_dist1[b] + red_dist2[i])

    # 검정점 i -> 빨간점 2 -> 빨간점 1 -> 검정점 i
    # 순으로 돌아오는 경우입니다.
    ans = min(ans, red_dist2[i] + red_dist2[a] + red_dist1[i])

# 불가능하다면 -1을 출력합니다.
if ans == INT_MAX:
    ans = -1

print(ans)