# 최댓값을 나타내는 상수입니다.
INF = 10**9

# n과 k 값을 입력받습니다.
n, k = map(int, input().split())

# 보물 지도의 정보를 입력받습니다.
a = [0] + list(map(int, input().split()))

# 동적 프로그래밍을 이용해 최대 합을 구합니다.
# dp[i][j] :: i번째 숫자를 마지막으로, 음수가 j번 나타났을 때 나타나는 연속합 중 최댓값
dp = [[-INF for _ in range(k + 1)] for _ in range(n + 1)]
ans = -INF

for i in range(1, n + 1):
    # a[i]가 0 이상인 경우
    if a[i] >= 0:
        for j in range(k + 1):
            dp[i][j] = max(dp[i - 1][j] + a[i], a[i])
            ans = max(ans, dp[i][j])
    # a[i]가 음수인 경우
    else:
        # 최대 k개 까지만 음수가 나타날 수 있게 관리합니다.
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + a[i], a[i])
            ans = max(ans, dp[i][j])

# 최종 결과를 출력합니다.
print(ans)