import sys
sys.setrecursionlimit(50000)

MAX_H = 16

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
depth = [0] * (n + 1)

# parent[h][i] : i번 노드에서 2^h번 부모를 따라 위로 올라갔을 때의 노드 번호를 관리합니다.
parent = [
    [0] * (n + 1)
    for _ in range(MAX_H + 1)
]

# n - 1개의 에지 정보를 입력받습니다.
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))

    edges[x].append(y)
    edges[y].append(x)


# 트리 순회를 진행합니다.
# 동시에 depth를 기록해줍니다.
def dfs(x):
    # 노드 x의 자식들을 살펴봅니다.
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True

            # depth값을 갱신해주며
            # 재귀적으로 탐색합니다.
            depth[y] = depth[x] + 1

            # 이때 y번 노드에서 1번(=2^0)번 부모를 따라 위로 올라갔을 때의 
            # 노드 번호는 x가 됩니다.
            parent[0][y] = x

            dfs(y)


# a와 b의 LCA를 구해줍니다.
def lca(a, b):
    # Step 0.
    # 노드 a의 높이가 더 같거나 커지도록 만들어줍니다.
    if depth[a] < depth[b]:
        return lca(b, a)

    # Step 1.
    # 노드 a의 높이를 노드 b의 높이까지 끌어올려줍니다.
    # 이는 십진수를 이진수로 빠르게 바꾸는 방법 중 하나인
    # 2의 거듭제곱 중 가장 큰 값을 계속 빼주는 원리를 이용합니다.
    for h in range(MAX_H, -1, -1):
        # a의 높이를 b에 맞추기 위해
        # 아직 2^h 만큼 더 끌어 올려줘도 된다면
        # 그만큼 올라갔을 때의 조상 값으로 변경해줍니다.
        if depth[a] - depth[b] >= (1 << h):
            a = parent[h][a]

    # 이미 a와 b가 일치한다면
    # 바로 그 값을 반환합니다.
    if a == b:
        return a

    # Step 2.
    # 두 노드 a, b가 일치해지기 직전까지
    # 위로 올라갑니다.
    # 이때 역시 해당 높이에 도달하기 위해 점프해야 하는 값을 x라 한다면
    # x라는 십진수를 이진수로 빠르게 바꾸는 방법 중 하나인
    # 2의 거듭제곱 중 가장 큰 값을 계속 빼주는 원리를 이용합니다.
    # 단, 그 시점을 찾기 위해]
    # 두 노드가 일치해지기 바로 직전까지 최대한 올라가는 방법으로 진행합니다.
    for h in range(MAX_H, -1, -1):
        if parent[h][a] != parent[h][b]:
            a = parent[h][a]
            b = parent[h][b]

    # 이제 a, b는
    # 같아지기 바로 직전의 위치까지 올라온 것이므로
    # 최종 답은 a의 부모가 됩니다.
    return parent[0][a]


# dfs 탐색을 진행하며
# 각 노드의 depth와 parent값을 계산합니다.
depth[1] = 1
visited[1] = True
dfs(1)

# parent값을 갱신해줍니다.
for h in range(1, MAX_H + 1):
    # 0 ~ h - 1까지는 이미 계산이 되어 있다는 전제 하에
    # 정점 i로부터 2^h번 위로 올라갔을 때의 위치는
    # 정점 i로부터 2^(h-1)번 위로 올라간 뒤, 
    # 다시 그 노드로부터 2^(h-1)번 위로 다시 올라가면 
    # O(1)에 바로 구해집니다.
    for i in range(1, n + 1):
        parent[h][i] = parent[h - 1][parent[h - 1][i]]

# q개의 질의에 대해 답을 구해줍니다.
q = int(input())
for _ in range(q):
    a, b = tuple(map(int, input().split()))

    print(lca(a, b))