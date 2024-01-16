n, r, c = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

lst = []
x, y = r-1, c-1
while True:
    flag = False
    value = grid[x][y]
    lst.append(value)
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and value < grid[nx][ny]:
            flag = True
            x, y = nx, ny
            break
    if not flag:
        break
print(*lst)