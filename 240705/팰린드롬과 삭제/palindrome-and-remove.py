import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
string = input()
n = len(string)

# dp[i][j] : [i, j] 구간으로 팰린드롬을 만들기 위해 제거해야 하는 최소 문자의 수
dp = [
    [0] * n
    for _ in range(n)
]

# 최솟값을 구해야 하므로 
# dp 초기값으로 아주 큰 값을 설정합니다.
for i in range(n):
    for j in range(n):
        dp[i][j] = INT_MAX

# 구간의 크기가 1인 경우 dp값이 0이 되어야 합니다.
# dp[i][i] = 0이 초기조건이 됩니다.
for i in range(n):
    dp[i][i] = 0

# 구간의 크기가 2인 경우 두 문자가 일치한다면 0,
# 그렇지 않다면 1이 됩니다.
for i in range(n - 1):
    dp[i][i + 1] = 0 if string[i] == string[i + 1] else 1

# dp는 미리 구해져 있는 작은 문제를 가지고 큰 문제를 풀어야 하므로
# 이러한 유형의 경우 구간을 점점 넓혀가면서 dp값을 채워야만 합니다. 
# 따라서 구간의 크기를 3부터 n까지 증가하게 미리 정해줍니다.
for gap in range(3, n + 1):
    # 구간의 시작위치 i를 정해줍니다.
    for i in range(n - gap + 1):
        # 구간의 크기와 시작 위치가 정해져 있기에
        # 끝 위치는 자동으로 정해집니다.
        j = i + gap - 1

        # [i, j]구간은
        # [i, j - 1] 구간에서 가장 뒤 1개를 자르거나,
        # [i + 1, j] 구간에서 가장 앞 1개를 자르거나,
        # str[i] == str[j]일때에만
        # [i + 1][j - 1] 구간의 값을 그대로 채용할 수 있습니다.

        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)

        if string[i] == string[j]:
            dp[i][j] = min(dp[i][j], dp[i + 1][j - 1])

# 전체 문자열에서 팰린드롬을 만들기 위해 제거해야 하는 최소 문자의 수를 출력합니다.
print(dp[0][n - 1])