# 변수 선언 및 입력:
string = input()
n = len(string)
ans = 1

# dp[i][j] : [i, j] 구간이 좌우대칭인 문자열이면 1 / 아니라면 0
dp = [
    [0] * n
    for _ in range(n)
]

# 구간의 크기가 1인 경우 dp값이 1이 되어야 합니다.
# dp[i][i] = 1이 초기조건이 됩니다.
for i in range(n):
    dp[i][i] = 1

# 구간의 크기가 2인 경우 두 문자 동일하면 1 
# 아니라면 0이 됩니다.
for i in range(n - 1):
    dp[i][i + 1] = int(string[i] == string[i + 1])
    if dp[i][i + 1]: ans = 2

# dp는 미리 구해져 있는 작은 문제를 가지고 큰 문제를 풀어야 하므로
# 이러한 유형의 경우 구간을 점점 넓혀가면서 dp값을 채워야만 합니다. 
# 따라서 구간의 크기를 3부터 n까지 증가하게 미리 정해줍니다.
for gap in range(3, n + 1):
    # 구간의 시작위치 i를 정해줍니다.
    for i in range(n - gap + 1):
        # 구간의 크기와 시작 위치가 정해져 있기에
        # 끝 위치는 자동으로 정해집니다.
        j = i + gap - 1

        # [i, j]가 팰린드롬이 되기 위해서는
        # [i + 1, j - 1]이 좌우대칭 문자열이여야 하며
        # string[i] == string[j]를 만족해야 합니다.

        if dp[i + 1][j - 1] and string[i] == string[j]:
            dp[i][j] = 1

            # [i, j]가 팰린드롬이라는 뜻은
            # gap 길이의 좌우대칭 문자열이 있다는 뜻입니다.
            # 정답을 갱신해줍니다.
            ans = gap

# 가장 긴 좌우대칭인 문자열의 길이를 출력합니다.
print(ans)