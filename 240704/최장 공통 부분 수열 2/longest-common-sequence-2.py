# 입력받은 두 문자열의 최장 공통 부분 수열(LCS)을 찾는 프로그램입니다.
a = input()
b = input()

n, m = len(a), len(b)
dp = [[0] * (m + 1) for _ in range(n + 1)]
path = [[(0, 0)] * (m + 1) for _ in range(n + 1)]

# dp 배열을 계산하고 각 단계에서의 경로를 추적합니다.
# dp[i][j] : 문자열 a를 i번째까지 확인하고, 문자열 b를 j번째까지 확인했을 때
# 최장 공통 부분 수열의 길이
# path[i][j] : 그러한 최장 공통 부분 수열이 어느 이전 정보에서 왔는지의 정보
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if dp[i][j] < dp[i - 1][j]:
            dp[i][j] = dp[i - 1][j]
            path[i][j] = (i - 1, j)

        if dp[i][j] < dp[i][j - 1]:
            dp[i][j] = dp[i][j - 1]
            path[i][j] = (i, j - 1)

        if a[i - 1] == b[j - 1] and dp[i][j] < dp[i - 1][j - 1] + 1:
            dp[i][j] = dp[i - 1][j - 1] + 1
            path[i][j] = (i - 1, j - 1)

# 최장 공통 부분 수열을 추적하여 결과를 구성합니다.
lcs = []
i, j = n, m
while i > 0 and j > 0:
    if path[i][j] == (i - 1, j - 1) and a[i - 1] == b[j - 1]:
        lcs.append(a[i - 1])
        i -= 1
        j -= 1
    else:
        i, j = path[i][j]

# 최장 공통 부분 수열을 출력합니다.
print(''.join(reversed(lcs)))