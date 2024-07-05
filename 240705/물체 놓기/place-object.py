import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

# 그래프에 있는 모든 노드들에 대해
# 초기값을 전부 아주 큰 값으로 설정
dist = [INT_MAX] * (n + 1) 

# 그래프를 인접행렬로 표현
# 더미 노드(0번 노드)를 만들어서 1번부터 n번까지 노드를 (직접 물체를 놓는 비용) 으로 연결합니다.
for i in range(1, n + 1):
    graph[0][i] = int(input())

for i in range(1, n + 1):
    graph[i] = [0] + list(map(int, input().split()))

# 시작위치(더미노드)에는 dist값을 0으로 설정
dist[0] = 0

# O(|V|^2) 프림 코드
ans = 0
for i in range(0, n + 1):
    # V개의 정점 중 
    # 아직 방문하지 않은 정점 중
    # dist값이 가장 작은 정점을 찾아줍니다.
    min_index = -1
    for j in range(0, n + 1):
        if visited[j]:
            continue
        
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j

    # 최솟값에 해당하는 정점에 방문 표시를 진행합니다.
    visited[min_index] = True

    # mst 값을 갱신해줍니다.
    ans += dist[min_index]

    # 최솟값에 해당하는 정점에 연결된 간선들을 보며
    # 시작점으로부터의 최솟값을 갱신해줍니다.
    for j in range(1, n + 1):
        dist[j] = min(dist[j], graph[min_index][j])

print(ans)