import sys
input = sys.stdin.readline
t = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
direction = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3,
}
def in_range(x, y, n):
    return 0<=x<n and 0<=y<n

def move_and_check_crash(grid, n):
    tmp = [[[0, -1] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            v, d = grid[x][y][0], grid[x][y][1]
            if v:
                nx, ny = x + dx[d], y + dy[d]
                if in_range(nx, ny, n):
                    tmp[nx][ny] = [tmp[nx][ny][0]+1, d]
                else:
                    tmp[x][y] = [tmp[x][y][0]+1, (d+2)%4]
    for i in range(n):
        for j in range(n):
            if tmp[i][j][0] > 1:
                tmp[i][j] = [0, -1]
    return tmp

for _ in range(t):
    n, m = map(int, input().split())
    grid = [[[0, -1] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x, y, d = input().split()
        x = int(x)-1; y = int(y)-1
        grid[x][y] = [1, direction[d]]
    for _ in range(2*n): #최대 2n시간
        grid = move_and_check_crash(grid, n)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j][0]:
                cnt += 1
    print(cnt)