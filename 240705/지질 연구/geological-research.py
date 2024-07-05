from collections import deque

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]

# 진입차수를 관리합니다.
indegree = [0] * (n + 1)

# pressure[i] : i번 지층의 압력도를 관리합니다.
pressure = [0] * (n + 1)

# max_pressure[i] : i번 지층이 받는 압력 중 최대 압력입니다.
# max_pressure_cnt[i] : i번 지층이 최대 압력으로 받는 지층 개수입니다.
max_pressure = [0] * (n + 1)
max_pressure_cnt = [0] * (n + 1)

# 위상정렬을 위한 큐를 관리합니다.
q = deque()

# 인접리스트로 관리합니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))

    edges[x].append(y) 
    indegree[y] += 1 # 진입차수를 갱신합니다.

# 처음 indegree 값이 0인 곳이 시작점이 됩니다.
# 이 노드들을 queue에 넣어줍니다.
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

        # 아무 압력도 받지 않는 지층입니다.
        # 해당 지층은 압력도가 1입니다.
        pressure[i] = 1

# 위상정렬을 진행합니다.
# queue에 원소가 남아있다면 계속 진행합니다.
while q:
    # 가장 앞에 있는 원소를 뽑아줍니다.
    x = q.popleft()

    # x에서 갈 수 있는 모든 곳을 탐색합니다.
    for y in edges[x]:
        # y번 압력의 정보를 갱신합니다.
        if max_pressure[y] < pressure[x]:
            max_pressure[y] = pressure[x]
            max_pressure_cnt[y] = 1
        elif max_pressure[y] == pressure[x]:
            max_pressure_cnt[y] += 1

        # 해당 노드의 indegree를 1만큼 감소시켜줍니다.
        indegree[y] -= 1

        # 비로소 indegree가 0이 되었다면
        # queue에 새로 넣어줍니다.
        if not indegree[y]:
            if max_pressure_cnt[y] == 1:
                pressure[y] = max_pressure[y]
            else:
                pressure[y] = max_pressure[y] + 1

            q.append(y)
            
# 모든 지층의 압력도 중에서
# 가장 큰 값을 출력합니다.
ans = 0
for i in range(1, n + 1):
    ans = max(ans, pressure[i])

print(ans)