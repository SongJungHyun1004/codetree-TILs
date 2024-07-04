# n, m, k 값을 입력받습니다.
n, m, kk = map(int, input().split())

# 초기 상태를 설정합니다.
dp = [[[0 for _ in range(205)] for _ in range(205)] for _ in range(15)]
for i in range(1, m + 1):
    dp[1][i][i] = 1

# 동적 프로그래밍을 사용하여 각 상태를 계산합니다.
# dp[i][j][k] :: i개의 마법석을 사용하고, 숫자의 합이 j이며, 이중 가장 마지막의 숫자가 k인 가짓수
for i in range(1, n):
    for j in range(1, m + 1):
        for k in range(1, m + 1):
            for l in range(1, k + 1):
                if j + l > m:
                    break
                dp[i + 1][j + l][l] += dp[i][j][k]
                dp[i + 1][j + l][l] = min(dp[i + 1][j + l][l], 10**9)

# 최종 결과를 계산하고 출력합니다.
cur_l = 1
cur_m = m
for i in range(n, 0, -1):
    while dp[i][cur_m][cur_l] < kk:
        kk -= dp[i][cur_m][cur_l]
        cur_l += 1
    print(cur_l, end=' ')
    cur_m -= cur_l