n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def bomb(box):
    for j in range(n):
        bombs = [box[i][j] for i in range(n-1, -1, -1)]
        while True:
            isExploded = False
            x = 0
            while x < len(bombs):
                y = x+1
                cnt = 1
                while y < len(bombs) and bombs[x] == bombs[y]:
                    cnt += 1
                    y += 1
                if cnt >= m:
                    isExploded = True
                    for _ in range(cnt):
                        bombs.pop(x)
                else:
                    x += 1
            if not isExploded:
                break
        for i in range(n):
            if i < len(bombs):
                box[n-1-i][j] = bombs[i]
            else:
                box[n-1-i][j] = 0
    return box
    
def rotate(box):
    tmp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = box[n-1-j][i]
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


for _ in range(k):
    box = bomb(grid)
    box = rotate(box)
    box = drop(box)
    grid = bomb(box)

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            ans += 1
print(ans)