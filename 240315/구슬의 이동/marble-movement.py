n, m, t, k = map(int, input().split())
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
direction = {
    'R':0,
    'D':1,
    'L':2,
    'U':3,
}
marbles = {}
for i in range(m):
    r, c, d, v = input().split()
    r=int(r)-1; c=int(c)-1; d=direction[d]; v=int(v)
    grid[r][c].append(i+1)
    marbles[i+1] = (r, c, v, d)

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def simulate():
    global marbles
    new_marbles = {}
    for num, info in marbles.items():
        x, y, v, d = info
        grid[x][y].remove(num)
        for _ in range(v):
            nx, ny = x + dxs[d], y + dys[d]
            if not in_range(nx, ny):
                d = (d+2)%4
                nx, ny = x + dxs[d], y + dys[d]
            x, y = nx, ny
        new_marbles[num] = (x, y, v, d)
        grid[x][y].append(num)
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) > k:
                lst = sorted(grid[i][j], key=lambda x:(new_marbles[x][2], x), reverse=True)
                while len(lst) > k:
                    del new_marbles[lst.pop()]
                grid[i][j] = lst
    marbles = new_marbles
    
for _ in range(t):
    simulate()

print(len(marbles))