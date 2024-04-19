n, k = map(int, input().split())
grid = [
    [0]*(n+1)
    for _ in range(n+1)
]
for i in range(1, n+1):
    grid[i][1:] = list(map(int, input().split()))

prefix = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i-1][j]+prefix[i][j-1]+grid[i][j]-prefix[i-1][j-1]

mx = 0
for i in range(1, n+2-k):
    for j in range(1, n+2-k):
        val = prefix[i+k-1][j+k-1]-prefix[i+k-1][j-1]-prefix[i-1][j+k-1]+prefix[i-1][j-1]
        mx = max(mx, val)
print(mx)