n, t = map(int, input().split())
commands = list(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

x, y, d = n//2, n//2, 0
def in_range(x, y):
    return 0<=x<n and 0<=y<n

ans = grid[x][y]
for cmd in commands:
    if cmd == 'R':
        d = (d+1)%4
    elif cmd == 'L':
        d = (d-1)%4
    elif cmd == 'F':
        nx, ny = x + dx[d], y + dy[d]
        if in_range(nx, ny):
            x, y = nx, ny
            ans += grid[x][y]

print(ans)