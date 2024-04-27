n = int(input())
grid = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    grid[i][1:] = list(map(int, input().split()))

prefix = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = grid[i][j]+prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]

mx = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(i, n+1):
            for l in range(j, n+1):
                s = prefix[k][l] - prefix[k][j-1] - prefix[i-1][l] + prefix[i-1][j-1]
                mx = max(mx, s)
print(mx)