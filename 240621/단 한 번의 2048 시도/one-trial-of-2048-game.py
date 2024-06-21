grid = [
    list(map(int, input().split()))
    for _ in range(4)
]
d = input()

def rotateL(box):
    tmp = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            tmp[i][j] = box[j][4-1-i]
    return tmp

def rotateR(box):
    tmp = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            tmp[i][j] = box[4-1-j][i]
    return tmp

def drop(box):
    tmp = [[0]*4 for _ in range(4)]
    for j in range(4):
        k = 3
        for i in range(3, -1, -1):
            if grid[i][j]:
                if i and grid[i][j] == grid[i-1][j]:
                    tmp[k][j] = 2*grid[i][j]
                    grid[i-1][j] = 0
                else:
                    tmp[k][j] = grid[i][j]
                k -= 1
    return tmp

if d == 'L':
    grid = rotateL(grid)
    grid = drop(grid)
    grid = rotateR(grid)
elif d == 'R':
    grid = rotateR(grid)
    grid = drop(grid)
    grid = rotateL(grid)
elif d == 'U':
    grid = rotateL(rotateL(grid))
    grid = drop(grid)
    grid = rotateR(rotateR(grid))
else:
    grid = drop(grid)

for i in range(4):
    print(*grid[i])