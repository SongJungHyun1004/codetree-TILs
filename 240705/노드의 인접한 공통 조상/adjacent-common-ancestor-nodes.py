import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
depth = [0] * (n + 1)

# n - 1개의 부모-자식 연결 관계 정보를 입력받습니다.
for _ in range(n - 1):
    p, x = tuple(map(int, input().split()))

    parent[x] = p
    edges[p].append(x)

# 가장 가까운 공통 조상을 구할 두 노드의 번호가 주어집니다.
a, b = tuple(map(int, input().split()))


# 트리 순회를 진행합니다.
# 동시에 depth를 기록해줍니다.
def dfs(x):
    # 노드 x의 자식들을 살펴봅니다.
    for y in edges[x]:
        # depth값을 갱신해주며
        # 재귀적으로 탐색합니다.
        depth[y] = depth[x] + 1
        dfs(y)

   
# 부모가 여전히 없는 노드가 루트 노드가 됩니다.
root_vertex = 0
for i in range(1, n + 1):
    if parent[i] == 0:
        root_vertex = i

# dfs 탐색을 진행하며
# 각 노드의 depth를 계산합니다.
depth[root_vertex] = 1
dfs(root_vertex)

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