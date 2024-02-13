n, m, r, c = map(int, input().split())
m_lst = list(input().split())
grid = [
    [0]*n
    for _ in range(n)
]
r-=1;c-=1
dice = [1,2,3]
grid[r][c] = 7-dice[0]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
dir_dict = {
    'L':2,
    'R':0,
    'U':3,
    'D':1
}
def in_range(x, y):
    return 0<=x<n and 0<=y<n
x, y = r, c
for d in m_lst:
    nx, ny = x + dxs[dir_dict[d]], y + dys[dir_dict[d]]
    if in_range(nx, ny):
        if d == 'L':
            dice[0], dice[2] = dice[2], 7-dice[0]
        elif d == 'R':
            dice[0], dice[2] = 7-dice[2], dice[0]
        elif d == 'U':
            dice[0], dice[1] = dice[1], 7-dice[0]
        elif d == 'D':
            dice[0], dice[1] = 7-dice[1], dice[0]
        grid[nx][ny] = 7-dice[0]
        x, y = nx, ny
ans = 0
for i in range(n):
    for j in range(n):
        ans += grid[i][j]
print(ans)