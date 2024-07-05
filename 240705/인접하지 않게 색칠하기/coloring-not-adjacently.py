import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    
    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append(y)
    edges[y].append(x)

a = [0] * (n + 1)

# n개의 노드에 적힌 값을 입력받습니다.
for i in range(1, n + 1):
    a[i] = int(input())

k = int(input())

dp = [
    [[0, 0] for _ in range(k + 1)]
    for _ in range(n + 1)
]
ans = 0


# 1번 노드를 시작으로 DFS를 진행하며 값을 갱신합니다.
# dp[x][i][j] = x번 노드를 루트로 하는 서브트리에서 i개를 색칠했을 때의 최댓값
# (j == 1일 경우 x번 노드를 색칠, j == 0일 경우 x번 노드를 색칠하지 않음)
def dfs(x):
    # 현재 노드를 최초로 색칠하는 경우에 대한 초기조건입니다.
    dp[x][1][1] = a[x]
    # 현재 노드를 칠하지 않는 경우에 대한 초기조건입니다.
    dp[x][0][0] = 0

    # 노드 x에 연결된 간선을 살펴보며 전부 방문해줍니다.
    for y in edges[x]:
        # 이미 방문한 정점이라면 스킵해줍니다.
        if visited[y]: 
            continue

        visited[y] = True
        dfs(y)

        # dp값들을 점화식에 따라 채워줍니다.

        # x번 노드를 색칠하는 경우이며 동시에 총 i개의 노드가 색칠되었기를 바라는 순간이라면
        # 지금까지의 자식들 가지고는 i - j개의 노드를 칠했으며 x번 노드 자체는 색칠이 되어야 하고
        # 자식 노드 y에서 정확히 j개의 노드를 칠하고 동시에 y번 노드 자체는 색칠이 되지 않아야 합니다.
        for i in range(k, 0, -1):
            for j in range(1, i + 1):
                dp[x][i][1] = max(dp[x][i][1], dp[x][i - j][1] + dp[y][j][0])

        # x번 노드를 색칠하지 않은 경우이며 동시에 총 i개의 노드가 색칠되었기를 바라는 순간이라면
        # 지금까지의 자식들 가지고는 i - j개의 노드를 칠했으며 x번 노드 자체는 색칠이 되지 않아야 하고
        # 자식 노드 y에서 정확히 j개의 노드를 칠하고 동시에 y번 노드 자체는 색칠이 되던 말던 상관이 없습니다.
        for i in range(k, -1, -1):
            for j in range(i + 1):
                dp[x][i][0] = max(dp[x][i][0], 
                                  dp[x][i - j][0] + 
                                  max(dp[y][j][0], dp[y][j][1]))


# 1번 노드를 시작으로 DFS를 진행하며 값을 갱신합니다.
visited[1] = True
dfs(1)

# 모든 dp의 값 중 최댓값을 출력합니다.
# 최대 i개의 노드를 색칠하는 경우를 전부 탐색합니다.
for i in range(1, k + 1):
    ans = max(ans, dp[1][i][0])
    ans = max(ans, dp[1][i][1])

print(ans)