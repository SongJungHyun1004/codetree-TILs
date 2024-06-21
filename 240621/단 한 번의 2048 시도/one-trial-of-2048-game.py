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
            if box[i][j]:
                tmp[k][j] = box[i][j]
                k -= 1
    tmp2 = [[0]*4 for _ in range(4)]
    for j in range(4):
        k = 3
        for i in range(3, -1, -1):
            if tmp[i][j]:
                if i and tmp[i][j] == tmp[i-1][j]:
                    tmp2[k][j] = 2*tmp[i][j]
                    tmp[i-1][j] = 0
                else:
                    tmp2[k][j] = tmp[i][j]
                k -= 1
    return tmp2

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