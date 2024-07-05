from collections import deque

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

edges = [[] for _ in range(n + 1)]

# 진입차수를 관리합니다.
indegree = [0] * (n + 1)

# 각 정점을 방문했는지 판단합니다.
visited = [False] * (n + 1)

# 위상정렬을 위한 큐를 관리합니다.
q = deque()

query = [(-1, -1)] * (m + 1)

# 각 입력을 순서대로 관리합니다.
for i in range(1, m + 1):
    query[i] = tuple(map(int, input().split()))

ans = 0


def cycle_exist(limit):
    # 변수를 초기화합니다.
    for i in range(1, n + 1):
        indegree[i] = 0
        edges[i] = []
        visited[i] = False

    # limit번까지의 간선이 존재할 때 모순이 있는지 없는지를 판단합니다.
    # 그래프를 인접 리스트로 관리합니다.
    for i in range(1, limit + 1):
        a, b = query[i]

        edges[a].append(b) 
        indegree[b] += 1 # 진입차수를 갱신합니다.

    # 처음 indegree 값이 0인 곳이 루트가 됩니다.
    # 이 노드들을 queue에 넣어주고, 정답으로 미리 저장해 놓습니다.
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

            # indegree가 0이 되었다면
            # queue에 새로 넣어줍니다.
            if not indegree[y]:
                q.append(y)

    # 모든 노드를 방문했다면 그래프 내에 사이클이 존재하지 않는다는 뜻입니다.
    is_cycle = False
    for i in range(1, n + 1):
        if not visited[i]: 
            is_cycle = True

    return is_cycle


# 답을 결정하고 이분 탐색을 진행합니다.
lo, hi = 1, m

while lo <= hi:
    mid = (lo + hi) // 2

    # 1번부터 mid번 정보까지 사용했을 때
    # 사이클이 존재한다면 입력에서 모순이 존재합니다.
    # 정답을 갱신하고 더 작은 답이 있는지 탐색합니다.
    if cycle_exist(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

if ans == 0:
    print("Consistent")
else:
    print(ans)