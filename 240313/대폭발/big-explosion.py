import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, m, r, c = map(int, input().split())
grid = [
    [0]*n
    for _ in range(n)
]
r-=1;c-=1
grid[r][c] = 1

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def simulate(pos_lst, t):
    if t > m:
        return
    offset = 2**(t-1)
    new_pos_lst = []
    for x, y in pos_lst:
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx*offset, y + dy*offset
            if in_range(nx, ny) and not grid[nx][ny]:
                grid[nx][ny] = 1
                new_pos_lst.append((nx, ny))
    pos_lst.extend(new_pos_lst)
    simulate(pos_lst, t+1)


t = 0
cnt = 0
pos_lst = [(r, c)]
simulate(pos_lst, t+1)
print(len(pos_lst))