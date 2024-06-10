n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
pos_lst = []
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            pos_lst.append((i, j))
bombs = []

dxs1 = [1,2,-1,-2]
dys1 = [0,0,0,0]
dxs2 = [1,0,-1,0]
dys2 = [0,1,0,-1]
dxs3 = [1,1,-1,-1]
dys3 = [1,-1,1,-1]

mx = 0

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def simulate(pos_lst, bombs):
    tmp = [[0]*n for _ in range(n)]
    for (x, y), bomb in zip(pos_lst, bombs):
        tmp[x][y] = -1
        if bomb == 1:
            for dx, dy in zip(dxs1, dys1):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    tmp[nx][ny] = -1
        elif bomb == 2:
            for dx, dy in zip(dxs2, dys2):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    tmp[nx][ny] = -1
        elif bomb == 3:
            for dx, dy in zip(dxs3, dys3):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    tmp[nx][ny] = -1
    cnt = 0
    for i in range(n):
        for j in range(n):
            if tmp[i][j] == -1:
                cnt += 1
    return cnt
def choose(i):
    global mx
    if i > len(pos_lst):
        cnt = simulate(pos_lst, bombs)
        mx = max(mx, cnt)
        return
    for nn in range(1, 4):
        bombs.append(nn)
        choose(i+1)
        bombs.pop()
choose(1)
print(mx)