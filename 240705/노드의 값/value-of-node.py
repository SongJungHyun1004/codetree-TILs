import sys
sys.setrecursionlimit(10000)

# 변수 선언 및 입력:
n = int(input())

# 초기값들이 주어집니다.
a = [0] + list(map(int, input().split()))
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

dp = [0] * (n + 1) # dp[i] : i를 루트로 하는 서브트리를 전부 처리했을 때 최종적으로 i가 가지게 되는 값

ans = 0

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    
    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append(y)
    edges[y].append(x)


# DFS를 통해 연결된 모든 정점을 순회합니다.
# 자식부터 그리디하게 1로 만들어주는게 최선입니다.
def dfs(x):
    global ans

    # dp값은 주어진 초기값이 됩니다.
    dp[x] = a[x]

    # 노드 x에 연결된 간선을 살펴보며 전부 방문해줍니다.
    for y in edges[x]:
        # 만약 y번 정점을 이미 방문했다면 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True
        dfs(y)

        # 자식들의 값들 전부 더해줍니다.
        # 이때 자식들은 1만 남기고 가져와줍니다.
        dp[x] += dp[y] - 1

    # dp[x]를 1로 만들기 위해 필요한 비용을 계산합니다.
    ans += abs(dp[x] - 1)


# 루트를 시작으로 DFS를 진행하며 값을 갱신합니다.
visited[1] = True
dfs(1)

print(ans)