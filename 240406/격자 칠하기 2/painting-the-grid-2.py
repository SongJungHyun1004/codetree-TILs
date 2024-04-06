n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

half = round(n*n/2)
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def dfs(x, y, visited, depth, mid):
    global size
    if depth == mid:
        return
    visited[x][y] = True
    size += 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and abs(grid[nx][ny]-grid[x][y]) <= mid:
            dfs(nx, ny, visited, depth+1, mid)
            visited[nx][ny] = False

def isPossible(mid):
    global size
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                size = 0
                dfs(i, j, visited, 0, mid)
                if half <= size:
                    return True
    return False

def binary_search():
    left = 0
    right = 10**6
    d = right
    while left <= right:
        mid = (left+right)//2
        if isPossible(mid):
            right = mid - 1
            d = min(d, mid)
        else:
            left = mid + 1
    return d

print(binary_search())