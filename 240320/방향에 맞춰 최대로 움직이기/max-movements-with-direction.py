n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
direct = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = map(int, input().split())
r-=1;c-=1

dxs = [0,-1,-1,0,1,1,1,0,-1]
dys = [0,0,1,1,1,0,-1,-1,-1]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def choose(x, y, value, d, dist):
    global mx
    mx = max(mx, dist)
    while True:
        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx, ny):
            if grid[nx][ny] > value:
                choose(nx, ny, grid[nx][ny], direct[nx][ny], dist+1)
        else:
            break
        x, y = nx, ny
mx = 0
choose(r, c, grid[r][c], direct[r][c], 0)
print(mx)