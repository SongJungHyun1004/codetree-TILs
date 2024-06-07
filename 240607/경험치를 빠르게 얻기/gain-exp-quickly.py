import sys

INT_MIN = -sys.maxsize
INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
exp_list, runtime_list = [0], [0]

for _ in range(n):
    exp, runtime = tuple(map(int, input().split()))
    exp_list.append(exp)
    runtime_list.append(runtime)

# 최대 수행시간을 계산합니다.
t = sum(runtime_list)

# dp[i][j] : i번째 퀘스트까지 고려헀을 때
#            지금까지 퀘스트를 진행하는 데 걸리는 시간의 총 합이 j일 때
#            얻을 수 있었던 최대 경험치
dp = [
    [0] * (t + 1)
    for _ in range(n + 1)
]

def initialize():
    # 최대를 구하는 문제이므로
    # INT_MIN을 초기값으로 넣어줍니다.
    for i in range(n + 1):
        for j in range(t + 1):
            dp[i][j] = INT_MIN
    
    # 초기조건은
    # 아직 아무런 퀘스트도 고려해보지 않은 상태입니다.
    # 현재 0번째 퀘스트까지 고려헀을 때
    # 수행시간은 0이었고, 이때 경험치 0을 얻게 됩니다.
    dp[0][0] = 0


initialize()

# 점화식에 따라
# 값을 채워줍니다.
for i in range(1, n + 1):
    for j in range(t + 1):
        # Case 1. 현재 퀘스트를 진행하여
        #         수행시간의 총 합이 j가 되기 위해서는
        #         i - 1번째 퀘스트 까지 수행시간이 j - runtime[i]가 되어야 합니다.
        if j - runtime_list[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - runtime_list[i]] + exp_list[i])
        
        # Case 2. 현재 퀘스트를 진행하지 않고
        #         수행시간의 총 합이 j가 되기 위해서는
        #         i - 1번째 퀘스트 까지 수행시간이 j가 되어야 합니다.
        dp[i][j] = max(dp[i][j], dp[i - 1][j])

# n개의 퀘스트까지 고려했을 때
# 최대 경험치 합이 m 이상인 경우 중
# 최소 시간을 계산합니다. 
ans = INT_MAX
for j in range(t + 1):
    if dp[n][j] >= m:
        ans = min(ans, j)

# 불가능하다면
# -1이 답이 됩니다.
if ans == INT_MAX:
    ans = -1

print(ans)