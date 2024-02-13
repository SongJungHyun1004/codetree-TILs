import sys
# 계단의 층 수를 입력받습니다.
n = int(input())
coin = [0] * (n + 1)

INT_MIN = -sys.maxsize
# 각 층의 동전의 개수를 입력받습니다.
coin = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(4)] for _ in range(n + 1)]

# 기본 케이스를 초기화합니다.
dp[1][0] = INT_MIN
dp[1][1] = coin[1]
dp[1][2] = INT_MIN
dp[1][3] = INT_MIN
if n > 1:
    dp[2][0] = coin[2]
    dp[2][1] = INT_MIN
    dp[2][2] = coin[1] + coin[2]
    dp[2][3] = INT_MIN

# 동적 프로그래밍을 사용하여 최대 가치를 계산합니다.
# dp[i][j] : i번 위치에 도착했을 때, 정확히 j번 1계단 올랐을 때의 최대 가치
for i in range(3, n + 1):
    for j in range(4):
        dp[i][j] = max(dp[i][j], dp[i - 2][j] + coin[i])
        if j:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coin[i])

# 가능한 모든 경우에서 최대 가치를 찾아 출력합니다.
ans = max(dp[n])
print(ans)