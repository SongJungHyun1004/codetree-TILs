n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

mx = 0
dx = [1,0,-1,0]
dy = [0,-1,0,1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def simulate():
    lst = []
    for j in range(n):
        t = 0
        x, y, d = -1, j, 0
        while True:
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny):
                if grid[nx][ny] == 1:
                    if d == 0 or d == 2:
                        d = (d+1)%4
                    else:
                        d = (d-1)%4
                elif grid[nx][ny] == 2:
                    d = 3 - d
                x, y = nx, ny
                t += 1
            else:
                lst.append(t+1)
                break
    return max(lst)

def rotate():
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[i][j] = grid[j][n-1-i]
            if ret[i][j] == 1:
                ret[i][j] = 2
            elif ret[i][j] == 2:
                ret[i][j] = 1
    return ret

for _ in range(4):
    t = simulate()
    mx = max(mx, t)
    grid = rotate()

print(mx)