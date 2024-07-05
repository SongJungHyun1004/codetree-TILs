import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n, r, q = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
size = [0] * (n + 1)

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    
    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append(y)
    edges[y].append(x)


# DFS를 통해 연결된 모든 정점을 순회합니다.
# 동시에 dp값을 계산해줍니다.
def dfs(x):
    size[x] = 1

    # 노드 x에 연결된 간선을 살펴보며 전부 방문해줍니다.
    for y in edges[x]:
        # 만약 y번 정점을 이미 방문했다면 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True
        dfs(y)

        # 자신의 자식 노드의 크기를 전부 더해 저장합니다.
        size[x] += size[y]


# 루트를 시작으로 DFS를 진행하며 값을 갱신합니다.
visited[r] = True
dfs(r)

# q개의 질의에 대해 올바른 답을 출력합니다.
for _ in range(q):
    x = int(input())

    # x번 노드에 대해, x번 노드를 루트로 하는
    # 서브트리의 크기를 출력합니다.
    print(size[x])