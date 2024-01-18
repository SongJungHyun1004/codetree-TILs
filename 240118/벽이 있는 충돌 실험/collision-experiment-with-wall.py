import copy
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
    
for _ in range(t):
    n, m = map(int, input().split())
    grid = [[[0, -1] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x, y, d = input().split()
        x = int(x)-1; y = int(y)-1
        grid[x][y] = [1, direction[d]]
    for tt in range(2*n): #최대 2n시간
        tmp = [[[0, -1] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                v, d = grid[i][j][0], grid[i][j][1]
                if v:
                    nx, ny = i + dx[d], j + dy[d]
                    if in_range(nx, ny):
                        tmp[nx][ny] = [tmp[nx][ny][0]+1, d]
                    else:
                        tmp[i][j] = [tmp[i][j][0]+1, (d+2)%4]
        for i in range(n):
            for j in range(n):
                if tmp[i][j][0] > 1:
                    tmp[i][j] = [0, -1]
        grid = copy.deepcopy(tmp)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j][0]:
                cnt += 1
    print(cnt)