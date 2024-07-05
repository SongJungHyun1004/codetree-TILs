from collections import deque

# 변수 선언 및 입력:
n, m1, m2 = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]

# 진입차수를 관리합니다.
indegree = [0] * (n + 1)

# 각 정점을 방문했는지 판단합니다.
visited = [False] * (n + 1)

# 위상정렬을 위한 큐를 관리합니다.
q = deque()

# 인접리스트로 관리합니다.
for _ in range(m1):
    x, y = tuple(map(int, input().split()))

    edges[x].append(y) 
    indegree[y] += 1 # 진입차수를 갱신합니다.

# 양방향 간선은 생각하지 않아도 괜찮습니다.
# 단방향 간선에 사이클이 없을 경우
# 양방향 간선은 위상정렬된 순서에 맞게 방향을 맞춰주면
# 항상 사이클이 없는 그래프가 됩니다.
# 반면 단방향 간선에 사이클이 있을 경우
# 양방향 간선을 어떻게 방향을 설정하더라도
# 해당 그래프에는 사이클이 존재합니다.
for _ in range(m2):
    a, b = tuple(map(int, input().split()))

# 처음 indegree 값이 0인 곳이 시작점이 됩니다.
# 이 노드들을 queue에 넣어줍니다.
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

# 위상정렬을 진행합니다.
# queue에 원소가 남아있다면 계속 진행합니다.
while q:
    # 가장 앞에 있는 원소를 뽑아줍니다.
    x = q.popleft()

    visited[x] = True

    # x에서 갈 수 있는 모든 곳을 탐색합니다.
    for y in edges[x]:
        # 해당 노드의 indegree를 1만큼 감소시켜줍니다.
        indegree[y] -= 1

        # 비로소 indegree가 0이 되었다면
        # queue에 새로 넣어줍니다.
        if not indegree[y]:
            q.append(y)

# 모든 노드를 방문했다면 그래프 내에 사이클이 존재하지 않는다는 뜻입니다.
is_cycle = False
for i in range(1, n + 1):
    if not visited[i]: 
        is_cycle = True

# 사이클이 존재하는지 여부를 출력합니다.
if is_cycle:
    print("No")
else:
    print("Yes")