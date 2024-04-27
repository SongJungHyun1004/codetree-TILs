n = int(input())
grid = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    grid[i][1:] = list(map(int, input().split()))

prefix = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = grid[i][j]+prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]

mx = float('-inf')
for i in range(1, n+1):
    for j in range(i, n+1):
        tmp = 0
        for k in range(1, n+1):
            s = prefix[j][k] - prefix[i-1][k] - prefix[j][k-1] + prefix[i-1][k-1]
            tmp = max(s, tmp+s)
            mx = max(mx, tmp)
print(mx)