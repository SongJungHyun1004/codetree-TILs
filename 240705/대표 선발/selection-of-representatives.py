n = int(input())

MAX_K = 100

peopleInGroup = [
    [] for _ in range(MAX_K + 1)
]

grp = [[0]] + [
    list(map(int, input().split()[1:]))
    for _ in range(n)
]

# 각 사람별로 어느 그룹에 들어가는지 기록해줍니다.
for i in range(1, n + 1):
    for people in grp[i]:
        peopleInGroup[people].append(i)

MOD = 10**4 + 7

# dp[i][j] : 
# 1번을 시작으로 i번 숫자까지 세었을 때
# 지금까지 쓴 그룹의 개수를 중복 없이
# x1, x2, ..., xk라 헀을 때 
# 2^x1 + 2^x2 + ... + 2^xk 값이 j인 (bitmask된 정수값이 j)
# 방법의 총 가짓수
dp = [
    [0 for _ in range(1 << n)]
    for _ in range(MAX_K + 1)
]


# 초기조건은
# 0번 숫자까지 세었을 때 아무것도 안 고른 상태입니다.
# 이 때에는 1을 넣어줍니다.
dp[0][0] = 1

# 뿌려주는 방식의 dp를 진행합니다.
# dp[i][j]가 계산이 되어있다는 가정하에서
# 그 다음 상태값을 갱신합니다.
for i in range(MAX_K):
    for j in range(1 << n):
        # dp값이 0이라면
        # 해당 값은 갱신할 필요가 없으니 패스합니다.
        if dp[i][j] == 0:
            continue

        # 그 다음 숫자 i + 1번을 어느 그룹에서 쓸지로 dp를 갱신합니다.

        # 우선 i + 1번을 안 쓰는 경우입니다. dp값을 그대로 갱신합니다.
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= MOD

        # i + 1번을 대표로 선발한다고 했을 때, i + 1번이 속한 모든 그룹에 대해
        # 각각 대표로 선발을 할 수 있는 가짓수를 갱신해줍니다.
        for idx in range(len(peopleInGroup[i + 1])):
            k = peopleInGroup[i + 1][idx]

            # 이미 k번 그룹이 채워져있으면 넘어갑니다.
            # 비트는 0번부터 이루어져 있으므로 번호들을 1 빼서 관리해줍니다.
            if (j >> (k - 1)) & 1: continue

            next_j = j + (1 << (k - 1))

            dp[i + 1][next_j] += dp[i][j]
            dp[i + 1][next_j] %= MOD

# 가능한 모든 경우의 수를 출력합니다.
print(dp[MAX_K][(1 << n) - 1])