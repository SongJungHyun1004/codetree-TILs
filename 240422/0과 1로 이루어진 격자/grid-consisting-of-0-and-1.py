n = int(input())
grid = [
    list(map(int, list(input())))
    for _ in range(n)
]

def push(x, y):
    for i in range(x+1):
        for j in range(y+1):
            grid[i][j] = 1 - grid[i][j]

cnt = 0
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if grid[i][j]:
            push(i, j)
            cnt += 1

print(cnt)