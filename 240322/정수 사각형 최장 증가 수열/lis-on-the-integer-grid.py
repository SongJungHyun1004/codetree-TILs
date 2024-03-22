import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# dp[x][y] = (x, y)에서 시작했을 때의 최대 길이
dp = [[-1 for _ in range(n)] for _ in range(n)]

def dfs(x, y):
    # 이미 계산된 경우 바로 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 1  # 자기 자신도 카운트
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    
    return dp[x][y]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)