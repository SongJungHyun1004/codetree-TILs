import sys

INT_MAX = sys.maxsize
MAX_G = 2500

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    [0] * (m + 1)
    for _ in range(n + 1)
]
renum = [
    [0] * (m + 1)
    for _ in range(n + 1)
]

# MST를 위해 필요한 변수입니다.
N = 0 # 새로운 그래프에서 정점의 개수를 의미합니다.
graph = [
    [0] * (MAX_G + 1)
    for _ in range(MAX_G + 1)
]
visited = [False] * (MAX_G + 1)

dist = [0] * (MAX_G + 1)

for i in range(1, n + 1):
    row = [0] + list(map(int, input().split()))
    for j in range(1, m + 1):
        grid[i][j] = row[j]


def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= m


def make_graph():
    global N

    # 새로운 그래프에서는 1의 개수 만큼 정점이 새로 생기게 됩니다.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j] == 1:
                N += 1
                renum[i][j] = N

    # graph 초기값을 불가능을 뜻하도록 큰 값을 넣어줍니다.
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = INT_MAX

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 1이라면 4방향으로 쭉 움직이며 (최초로 1이 되는 위치까지의 거리 - 1)이 가중치인 간선을 만들어줍니다.
            # 즉, 인접한 1끼리는 가중치가 0이 됩니다.
            if grid[i][j] == 1:
                for dx, dy in zip(dxs, dys):
                    dist = 1
                    while True:
                        nx, ny = i + dx * dist, j + dy * dist

                        if not in_range(nx, ny):
                            break
                        
                        if grid[nx][ny] == 1:
                            graph[renum[i][j]][renum[nx][ny]] = dist - 1 
                            break

                        dist += 1

   
make_graph()

# 그래프에 있는 모든 노드들에 대해
# 초기값을 전부 아주 큰 값으로 설정
for i in range(1, N + 1):
    dist[i] = INT_MAX

# 시작위치에는 dist값을 0으로 설정
dist[1] = 0

# O(|V|^2) 프림 코드
ans = 0
for i in range(1, N + 1):
    # V개의 정점 중 
    # 아직 방문하지 않은 정점 중
    # dist값이 가장 작은 정점을 찾아줍니다.
    min_index = -1
    for j in range(1, N + 1):
        if visited[j]:
            continue
        
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j

    # 다 해결하지 못했는데 그 다음 노드가 없다면
    # 답은 -1이 됩니다.
    if dist[min_index] == INT_MAX:
        ans = -1
        break

    # 최솟값에 해당하는 정점에 방문 표시를 진행합니다.
    visited[min_index] = True

    # mst 값을 갱신해줍니다.
    ans += dist[min_index]

    # 최솟값에 해당하는 정점에 연결된 간선들을 보며
    # 시작점으로부터의 최솟값을 갱신해줍니다.
    for j in range(1, N + 1):
        dist[j] = min(dist[j], graph[min_index][j])

print(ans)