import sys
sys.setrecursionlimit(10000)

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# n개의 노드에 적힌 값을 입력받습니다.
a = [0] + list(map(int, input().split()))

dp = [[0, 0] for _ in range(n + 1)]

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))

    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append(y)
    edges[y].append(x)


# 1번 노드를 시작으로 DFS를 진행하며 값을 갱신합니다.
# dp[i][j] = i번 노드를 루트로 하는 서브트리에서
# (j == 1일 때) i번 노드를 선택했을때의 값의 합의 최댓값
# (j == 0일 때) i번 노드를 선택하지 않았을 때의 값의 합의 최댓값
def dfs(x):
    # x번 노드가 포함된 경우 합은 a[x]가 포함됩니다.
    dp[x][1] = a[x]

    # 노드 x에 연결된 간선을 살펴보며 전부 방문해줍니다.
    for y in edges[x]:
        # 이미 방문한 정점이라면 스킵해줍니다.
        if visited[y]: 
            continue

        visited[y] = True
        dfs(y)

        # x번 노드가 포함된 경우 y번 노드는 포함될 수 없습니다.
        # x번 노드가 포함되지 않은 경우 y번 노드는 포함될 수도,
        # 포함되지 않을 수도 있습니다.
        dp[x][1] += dp[y][0]
        dp[x][0] += max(dp[y][0], dp[y][1])


# 1번 노드를 시작으로 DFS를 진행하며 값을 갱신합니다.
# dp[i][j] = i번 노드를 루트로 하는 서브트리에서
# (j == 1일 때) i번 노드를 선택했을때의 값의 합의 최댓값
# (j == 0일 때) i번 노드를 선택하지 않았을 때의 값의 합의 최댓값
visited[1] = True
dfs(1)

# 루트 노드에서 얻을 수 있는 최댓값
print(max(dp[1][0], dp[1][1]))