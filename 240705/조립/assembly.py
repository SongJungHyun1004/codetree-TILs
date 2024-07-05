from collections import deque

MOD = 1000000007

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]

# 진입차수를 관리합니다.
indegree = [0] * (n + 1)

# needs[i][j] : i번 조각을 만들기 위해 필요한 j번 조각의 수 (가장 작은 조각만)
needs = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

# 위상정렬을 위한 큐를 관리합니다.
q = deque()

# 인접리스트로 관리합니다.
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))

    edges[y].append((x, z))
    indegree[x] += 1 # 진입차수를 갱신합니다.

# 처음 indegree 값이 0인 곳이 시작점이 됩니다.
# 이 노드들을 queue에 넣어줍니다.
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

        # 해당 조각은 작은 조각이므로 dp를 갱신해줍니다.
        needs[i][i] = 1

# 위상정렬을 진행합니다.
# queue에 원소가 남아있다면 계속 진행합니다.
while q:
    # 가장 앞에 있는 원소를 뽑아줍니다.
    x = q.popleft()

    # x에서 갈 수 있는 모든 곳을 탐색합니다.
    for y, num in edges[x]:
        # y번 조각을 만들기 위해 필요한
        # 작은 조각의 수 정보를 갱신합니다.
        for j in range(1, n + 1):
            needs[y][j] += num * needs[x][j]

        # 해당 노드의 indegree를 1만큼 감소시켜줍니다.
        indegree[y] -= 1

        # 비로소 indegree가 0이 되었다면
        # queue에 새로 넣어줍니다.
        if not indegree[y]:
            q.append(y)

# n번 조각을 완성하는데 필요한 작은 조각들의 정보를 출력합니다.
for i in range(1, n + 1):
    if needs[n][i]:
        print(i, needs[n][i])