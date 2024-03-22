n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def dp_with_lower_bound(lower_bound):
    dp = [[float('inf')] * n for _ in range(n)]
    if grid[0][0] >= lower_bound:
        dp[0][0] = grid[0][0]  # 시작점 초기화

    for x in range(n):
        for y in range(n):
            if grid[x][y] < lower_bound:
                continue  # lower_bound 미만의 값은 사용하지 않음
            if x > 0:
                dp[x][y] = min(dp[x][y], max(dp[x-1][y], grid[x][y]))
            if y > 0:
                dp[x][y] = min(dp[x][y], max(dp[x][y-1], grid[x][y]))

    return dp[n-1][n-1]

answer = float('inf')
for x in range(n):
    for y in range(n):
        # 각 위치의 값들을 lower_bound로 설정
        lower_bound = grid[x][y]
        max_in_path = dp_with_lower_bound(lower_bound)
        if max_in_path != float('inf'):
            answer = min(answer, max_in_path - lower_bound)

print(answer)