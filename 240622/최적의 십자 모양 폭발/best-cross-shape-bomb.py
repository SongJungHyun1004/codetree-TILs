n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bomb(box, x, y):
    tmp = [[box[i][j] for j in range(n)] for i in range(n)]
    size = tmp[x][y]
    dxs = [0,1,0,-1]
    dys = [1,0,-1,0]
    for i in range(size):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx*i, y + dy*i
            if in_range(nx, ny):
                tmp[nx][ny] = 0
    return tmp

def drop(box):
    tmp = [[0]*n for _ in range(n)]
    for j in range(n):
        k = n-1
        for i in range(n-1, -1, -1):
            if box[i][j]:
                tmp[k][j] = box[i][j]
                k -= 1
    return tmp

def countPair(box):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not box[i][j]:
                continue
            nx1, ny1 = i+1, j
            if in_range(nx1, ny1) and box[i][j] == box[nx1][ny1]:
                cnt += 1
            nx2, ny2 = i, j+1
            if in_range(nx2, ny2) and box[i][j] == box[nx2][ny2]:
                cnt += 1
    return cnt

mx = 0
for i in range(n):
    for j in range(n):
        box = bomb(grid, i, j)
        box = drop(box)
        mx = max(mx, countPair(box))
print(mx)