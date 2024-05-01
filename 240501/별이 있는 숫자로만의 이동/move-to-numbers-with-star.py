import sys
input = sys.stdin.readline

n, k = map(int, input().split())
grid = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    grid[i][1:] = list(map(int, input().split()))

prefix = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = grid[i][j]+prefix[i][j-1]

def calculate(x, y):
    summation = 0
    summation += prefix[x][min(n, y+k)]-prefix[x][max(0, y-k-1)]
    a = k
    for i in range(1, k+1):
        a -= 1
        if x-i > 0:
            summation += prefix[x-i][min(n, y+a)]-prefix[x-i][max(0, y-a-1)]
        if x+i <= n:
            summation += prefix[x+i][min(n, y+a)]-prefix[x+i][max(0, y-a-1)]
    return summation
    
mx = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        val = calculate(i, j)
        mx = max(mx, val)
print(mx)