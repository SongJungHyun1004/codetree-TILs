n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0<=x<n and 0 <=y<n

def get_end_idx_of_explosion(start_idx, numbers):
    curr_num = numbers[start_idx]
    for end_idx in range(start_idx + 1, len(numbers)):
        if numbers[end_idx] != curr_num:
            return end_idx - 1
        
    return len(numbers) - 1

def canExplode():
    for j in range(n):
        numbers = [grid[i][j] for i in range(n)]
        curr_idx = 0
        while curr_idx < len(numbers):
            end_idx = get_end_idx_of_explosion(curr_idx, numbers)
            if end_idx - curr_idx + 1 >= m:
                if numbers[curr_idx]:
                    return True
            curr_idx = end_idx + 1
    return False

def explode():
    for j in range(n):
        while True:
            flag = False
            bombs = [grid[i][j] for i in range(n)]
            old = bombs[:]
            bombs = bombs[::-1]
            curr_idx = 0
            while curr_idx < len(bombs):
                end_idx = get_end_idx_of_explosion(curr_idx, bombs)
                if end_idx - curr_idx + 1 >= m:
                    bombs[curr_idx:end_idx + 1] = [0]*(end_idx - curr_idx + 1)
                    if bombs[curr_idx]:
                        flag = True
                curr_idx = end_idx + 1
            bombs = bombs[::-1]
            if old == bombs and not flag:
                break
            for i in range(n):
                grid[i][j] = bombs[i]
    
def drop():
    for j in range(n):
        tmp = [0]*n
        k = 0
        for i in range(n-1, -1, -1):
            if grid[i][j]:
                tmp[k] = grid[i][j]
                k += 1
        for i, v in enumerate(tmp[::-1]):
            grid[i][j] = v

def rotate():
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[i][j] = grid[n-1-j][i]
    return ret

for kk in range(k):
    while canExplode():
        explode()
        drop()
    grid = rotate()
    drop()
explode()
drop()

cnt = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            cnt += 1

print(cnt)