n = int(input())

MAX_K = 10
MOD = 10**4 + 7

# dp[i][j][k] : 
# 1번을 시작으로 i번 자릿수까지 세었을 때
# 각 자릿수별로 나온 숫자들을 중복 없이
# x1, x2, ..., xk라 헀을 때 
# 2^x1 + 2^x2 + ... + 2^xk 값이 j고 (bitmask된 정수값이 j)
# 마지막 숫자값이 k인 가짓수
dp = [
    [
        [0 for _ in range(MAX_K)]
        for _ in range(1 << MAX_K)
    ]
    for _ in range(n + 1)
]

   
# 초기조건은
# 1개를 1 ~ 9 중 하나로 고른 상태입니다.
# 이 때에는 1을 넣어줍니다.
for i in range(1, 10):
    dp[1][(1 << i)][i] = 1

# 뿌려주는 방식의 dp를 진행합니다.
# dp[i][j]가 계산이 되어있다는 가정하에서
# 그 다음 상태값을 갱신합니다.
for i in range(1, n):
    for j in range(1 << MAX_K):
        for k in range(MAX_K):
            # dp값이 0이라면
            # 해당 값은 갱신할 필요가 없으니 패스합니다.
            if dp[i][j][k] == 0:
                continue

            # 그 다음 숫자를 각각 (k - 1, k + 1)번 숫자를
            # 쓰게 되는 경우를 비교하여 갱신해줍니다.
            if 0 <= k - 1:
                dp[i + 1][j | (1 << (k - 1))][k - 1] += dp[i][j][k]
                dp[i + 1][j | (1 << (k - 1))][k - 1] %= MOD

            if k + 1 < MAX_K:
                dp[i + 1][j | (1 << (k + 1))][k + 1] += dp[i][j][k]
                dp[i + 1][j | (1 << (k + 1))][k + 1] %= MOD

# 가능한 모든 경우의 수를 출력합니다.
ans = 0
for i in range(MAX_K):
    ans += dp[n][(1 << MAX_K) - 1][i]
    ans %= MOD
print(ans)