import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [0] * (n + 1)
depth = [0] * (n + 1)

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
        # 이미 방문한 노드라면 패스합니다.
        if visited[y]:
            continue

        # depth값을 갱신해주며
        # 재귀적으로 탐색합니다.
        visited[y] = True
        depth[y] = depth[x] + 1
        parent[y] = x
        dfs(y)


# dfs 탐색을 진행하며
# 각 노드의 depth를 계산합니다.
visited[1] = True
depth[1] = 1
dfs(1)

# q개의 쿼리가 주어집니다.
q = int(input())
for _ in range(q):
    # 가장 가까운 공통 조상을 구할 두 노드의 번호가 주어집니다.
    a, b = tuple(map(int, input().split()))
   
    # Step 1.
    # 두 노드 a, b의 depth를 비교하며
    # depth가 더 큰 쪽을 위로 올리는 것을 반복하며 두 노드의 depth를 맞춰줍니다.
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    # Step 2.
    # 두 노드 a, b가 일치해질떄까지
    # 한 칸씩 위로 올라갑니다.
    while a != b:
        a = parent[a]
        b = parent[b]

    # LCA 값을 출력합니다.
    print(a)