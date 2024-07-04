# 두 문자열을 입력받습니다.
a = input()
b = input()

n = len(a)
m = len(b)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

# dp 배열을 초기화합니다.
for i in range(1, n+1):
    dp[i][0] = i
for j in range(1, m+1):
    dp[0][j] = j

# 두 문자열의 각 문자를 비교하며 동적 프로그래밍을 완성합니다.
# dp[i][j] :: a문자열의 처음 i개 문자열을, b문자열의 처음 j개로 바꾸는데 필요한 최소 연산 횟수
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            # 문자가 같으면 이전 편집 거리를 가져옵니다.
            dp[i][j] = dp[i-1][j-1]
        else:
            # 문자가 다르면 문자를 삽입하거나 삭제해야 합니다.
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

# 결과를 출력합니다.
print(dp[n][m])