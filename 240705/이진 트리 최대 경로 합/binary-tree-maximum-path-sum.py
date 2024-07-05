import sys
sys.setrecursionlimit(30000)

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
a = [0] * (n + 1)
dp = [0] * (n + 1)
max_length = [0] * (n + 1)
ans = 0

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    
    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append(y)
    edges[y].append(x)

# n개의 노드에 적힌 값을 입력받습니다.
for i in range(1, n + 1):
    a[i] = int(input())


# 1번 노드를 시작으로 DFS를 진행하며 값을 갱신합니다.
# dp[i] = i번 노드를 루트로 하는 서브트리에서 
# i번 노드를 끝으로 하는 경로 중 최대 합에 해당하는 경로
# max_length[i] = i번 노드를 루트로 하는 서브트리에서
# 두 자식노드로 이어지는 경로의 최댓갑
def dfs(x):
    # 이진트리므로 최대 자식 개수는 2개입니다.
    # 자식의 번호를 관리합니다.
    children = []

    # 노드 x에 연결된 간선을 살펴보며 전부 방문해줍니다.
    for y in edges[x]:
        # 이미 방문한 정점이라면 스킵해줍니다.
        if visited[y]: 
            continue

        visited[y] = True
        dfs(y)

        # y번 노드의 경로의 길이를 path에 추가해줍니다.
        children.append(y)

    # 왼쪽, 오른쪽 자식 번호를 기입해줍니다.
    # 만약 없다면 index가 0이 되도록 하여 후보 계산이 dp[0] = 0값을 이용하여
    # 답에 영향을 주지 않도록 합니다.
    left = children[0] if len(children) > 0 else 0
    right = children[1] if len(children) > 1 else 0

    # dp와 max_length를 갱신합니다.
    # dp의 경우 왼쪽 오른쪽 자식 중 값이 더 큰 경우에 현재 노드에 적혀있는 값을 추가합니다.
    # 단, 그 값이 음수라면 연결하지 않는 상태를 의미하는 0이 더 좋습니다.
    dp[x] = a[x] + max(0, max(dp[left], dp[right]))
    
    # max_length의 경우 현재 노드 + 왼쪽에서 얻을 수 있는 최대 + 오른쪽에서 얻을 수 있는 최대가 됩니다.
    max_length[x] = a[x] + max(0, dp[left]) + max(0, dp[right])

   
# 1번 노드를 시작으로 DFS를 진행하며 값을 갱신합니다.
visited[1] = True
dfs(1)

# 모든 max_length의 값 중 최댓값을 출력합니다.
for i in range(1, n + 1):
    ans = max(ans, max_length[i])

print(ans)