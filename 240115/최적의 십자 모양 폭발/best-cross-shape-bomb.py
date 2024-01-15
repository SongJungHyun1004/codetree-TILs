import copy
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
tmp = []

dxs = [0,-1,0,1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def explode(x, y):
    v = tmp[x][y]
    tmp[x][y] = 0
    for dx, dy in zip(dxs, dys):
        for i in range(1, v):
            nx, ny = x + dx * i, y + dy * i
            if in_range(nx, ny):
                tmp[nx][ny] = 0

def drop():
    for j in range(n):
        t = [0]*n
        k = 0
        for i in range(n-1, -1, -1):
            if tmp[i][j]:
                t[k] = tmp[i][j]
                k += 1
        for i, v in enumerate(t[::-1]):
            tmp[i][j] = v

def countPair():
    cnt = 0
    for i in range(n-1):
        for j in range(n-1):
            if tmp[i][j]:
                if tmp[i][j] == tmp[i+1][j]:
                    cnt += 1
                if tmp[i][j] == tmp[i][j+1]:
                    cnt += 1
    t = [tmp[i][n-1] for i in range(n)]
    for i in range(n-1):
        if t[i] and t[i] == t[i+1]:
            cnt += 1
    t = tmp[n-1][:]
    for i in range(n-1):
        if t[i] and t[i] == t[i+1]:
            cnt += 1
    return cnt

mx = 0
for i in range(n):
    for j in range(n):
        tmp = copy.deepcopy(grid)
        explode(i, j)
        drop()
        mx = max(mx, countPair())

print(mx)