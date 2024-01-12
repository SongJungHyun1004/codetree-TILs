n = 4
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
d = input()

def rotateR():
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[i][j] = grid[j][n-1-i]
    return ret

if d == 'U':
    grid = rotateR()
elif d == 'R':
    grid = rotateR()
    grid = rotateR()
elif d == 'D':
    grid = rotateR()
    grid = rotateR()
    grid = rotateR()

for i in range(n):
    tmp = [0]*n
    k = 0
    for j in range(n):
        if grid[i][j]:
            tmp[k] = grid[i][j]
            k += 1
    grid[i] = tmp[:]

for i in range(n):
    tmp = [0]*n
    k = 0
    flag = 0
    for j in range(n-1):
        if flag:
            flag = 0
            continue
        nxt = grid[i][j+1]
        if nxt == grid[i][j]:
            tmp[k] = nxt + grid[i][j]
            grid[i][j+1] = -1
            flag = 1
        else:
            tmp[k] = grid[i][j]
        k += 1
    if grid[i][n-2] != grid[i][n-1] and -1 != grid[i][n-1]:
        tmp[k] = grid[i][n-1]
    grid[i] = tmp[:]

if d == 'U':
    grid = rotateR()
    grid = rotateR()
    grid = rotateR()    
elif d == 'R':
    grid = rotateR()
    grid = rotateR()
elif d == 'D':
    grid = rotateR()

for i in range(n):
    print(*grid[i])