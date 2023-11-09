n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
mx = float('-inf')
for i in range(n):
    for j in range(n-2):
        cnt1 = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        for k in range(i+1, n):
            for l in range(n-2):
                cnt2 = grid[k][l] + grid[k][l+1] + grid[k][l+2]
                mx = max(mx, cnt1 + cnt2)
print(mx)