import copy
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
def in_range(x, y):
    return 0<=x<n and 0<=y<n
    
def move():
    tmp = [[[0, -1] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            v, d = grid[x][y][0], grid[x][y][1]
            if v:
                nx, ny = x + dx[d], y + dy[d]
                if in_range(nx, ny):
                    tmp[nx][ny] = [tmp[nx][ny][0]+1, d]
                else:
                    tmp[x][y] = [tmp[x][y][0]+1, (d+2)%4]
    return tmp

def check_crash(tmp):
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
        tmp = move()
        tmp = check_crash(tmp)
        grid = copy.deepcopy(tmp)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j][0]:
                cnt += 1
    print(cnt)