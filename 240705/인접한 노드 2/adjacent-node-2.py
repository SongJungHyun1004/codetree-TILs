import sys
sys.setrecursionlimit(10000)

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
ans_path = []

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


# 실제 DP의 값을 DFS2를 진행하여 역추적합니다.
def dfs2(x, tp):
    # tp가 1인 경우 x가 정답에 포함되어 있습니다. 정답 경로에 추가해줍니다.
    if tp == 1: 
        ans_path.append(x)

    # 노드 x에 연결된 간선을 살펴보며 전부 방문해줍니다.
    for y in edges[x]:
        # 이미 방문한 정점이라면 스킵해줍니다.
        if visited[y]: 
            continue
        
        visited[y] = True

        # tp가 1인 경우 tp가 0인 서브트리가 최선이므로 그 방향으로 이동합니다.
        if tp == 1:
            dfs2(y, 0)
        # tp가 0인 경우 자식노드들은 0과 1중 더 큰 값이 넘어가므로 해당 방향으로 이동합니다.
        else:
            if dp[y][0] > dp[y][1]:
                dfs2(y, 0)
            else:
                dfs2(y, 1)


# 1번 노드를 시작으로 DFS를 진행하며 값을 갱신합니다.
# dp[i][j] = i번 노드를 루트로 하는 서브트리에서
# (j == 1일 때) i번 노드를 선택했을때의 값의 합의 최댓값
# (j == 0일 때) i번 노드를 선택하지 않았을 때의 값의 합의 최댓값
visited[1] = True
dfs(1)

# DFS를 다시 진행하며 DP 최적의 값이 나온 Path를 추적합니다.
for i in range(1, n + 1):
    visited[i] = False

# 최적의 답이 나오는 경로를 선택합니다
visited[1] = True
if dp[1][0] > dp[1][1]:
    dfs2(1, 0)
else:
    dfs2(1, 1)

# 경로를 오름차순으로 정렬해줍니다.
ans_path.sort()

# 루트 노드에서 얻을 수 있는 최댓값
print(max(dp[1][0], dp[1][1]))
for num in ans_path:
    print(num, end=" ")