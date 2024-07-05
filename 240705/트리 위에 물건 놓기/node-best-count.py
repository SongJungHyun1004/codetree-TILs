import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [0] * (n + 1)

# dp[i][j] : i번 노드의 서브트리에서
#            j = 0이면 정확히 i번 노드에는 물건을 놓지 않은 상황
#            j = 1이면 정확히 i번 노드에는 물건을 내려놓은 상황이라고 했을 때
#            해당 상황에서 조건을 만족하며 최소한으로 놓았을 때 필요한 물건의 수
dp = [
    [0, 0]
    for _ in range(n + 1)
]

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
        if not visited[y]:
            visited[y] = True
            parent[y] = x
            dfs(y)

    # 이제 퇴각하기 전에
    # 각각의 자식들을 다시 순회하며 
    # dp[x][0], dp[x][1] 값을 갱신해줍니다.
    dp[x][0] = 0 # x 노드에 아무 물건도 놓지 않는 경우입니다. 
    dp[x][1] = 1 # x 노드에 물건을 놓는 경우이므로, 시작 값은 x에 놓은 물건의 수인 1이 됩니다.

    for y in edges[x]:
        # y가 x의 자식이 아니라면 패스합니다.
        if parent[y] != x:
            continue

        # Case 1. 
        # x번 노드에 물건을 놓지 않는 dp[x][0] 상황에서는
        # x의 자식들 y에 대해서는 j가 1인 경우만 선택이 가능하므로
        # dp[y][0]값들을 전부 더해주면 됩니다.
        dp[x][0] += dp[y][1]

        # Case 2. 
        # x번 노드에 물건을 놓는 dp[x][1] 상황에서는
        # x의 자식들 y에 대해서는 j가 0, 1 경우 전부 선택이 가능하므로
        # 최솟값을 전부 더해주면 됩니다.
        dp[x][1] += min(dp[y][0], dp[y][1])


# 1번 정점을 루트로 하는 트리를 만들어 문제를 해결합니다.
# 1번 정점을 시작으로 DFS를 진행하며 dp값을 갱신합니다.
visited[1] = True
dfs(1)

# dp[1][0], dp[1][1] 중 최솟값을 출력합니다.
print(min(dp[1][0], dp[1][1]))