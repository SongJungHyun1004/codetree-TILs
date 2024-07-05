from collections import deque

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]

# 진입차수를 관리합니다.
indegree = [0] * (n + 1)

# 각 일을 끝내는데 걸리는 시간을 관리합니다.
working_time = [0] * (n + 1)

# dp[i] : i번 일을 완료하기 위해 필요한 최소 시간을 관리합니다.
dp = [0] * (n + 1)

# 위상정렬을 위한 큐를 관리합니다.
q = deque()

for i in range(1, n + 1):
    working_time[i], _, *nums = tuple(map(int, input().split()))
    
    for x in nums:
        # 인접리스트로 관리합니다.
        edges[x].append(i)
        indegree[i] += 1 # 진입차수를 갱신합니다.
           

# 처음 indegree 값이 0인 곳이 시작점이 됩니다.
# 이 노드들을 queue에 넣어줍니다.
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)
        
        # 이때의 i 값들이 dp의 초기조건이 되며,
        # i번째 작업을 끝내기 위해서는 working_time[i] 만큼의 시간이 필요합니다.
        dp[i] = working_time[i]

# 위상정렬을 진행합니다.
# queue에 원소가 남아있다면 계속 진행합니다.
while q:
    # 가장 앞에 있는 원소를 뽑아줍니다.
    x = q.popleft()
    
    # x에서 갈 수 있는 모든 곳을 탐색합니다.
    for y in edges[x]:
        # y번째 작업이 완료되기 위해서는
        # 작업 중 가장 오래 걸리는 시간을 계속 기록해줘야하므로
        # 최댓값을 갱신해줍니다.
        # x일이 끝나기 위한 최소 시간이 dp[x]이므로
        # 이 일 직후 y일을 진행했을 때 걸리는 시간은
        # dp[x] + working_time[y]가 됩니다.
        dp[y] = max(dp[y], dp[x] + working_time[y])

        # 해당 노드의 indegree를 1만큼 감소시켜줍니다.
        indegree[y] -= 1

        # 비로소 indegree가 0이 되었다면
        # queue에 새로 넣어줍니다.
        if not indegree[y]:
            q.append(y)

# 각 일을 끝내는 데 걸리는 시간 중
# 최댓값이
# 모든 작업을 완료하기 위한 시간이 됩니다.
ans = 0
for i in range(1, n + 1):
    ans = max(ans, dp[i])

print(ans)