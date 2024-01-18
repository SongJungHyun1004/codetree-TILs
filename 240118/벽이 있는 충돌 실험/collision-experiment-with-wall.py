import sys
input = sys.stdin.readline
t = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
direction = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3,
}
def in_range(x, y, n):
    return 0<=x<n and 0<=y<n

for _ in range(t):
    n, m = map(int, input().split())
    grid = {}
    for _ in range(m):
        x, y, d = input().split()
        x = int(x)-1; y = int(y)-1
        grid[(x, y)] = direction[d]
    
    for _ in range(2*n): #최대 2n시간
        new_grid = {}
        to_remove = set()
        for (x, y), d in grid.items():
            nx, ny = x + dx[d], y + dy[d]
            if not in_range(nx, ny, n): # 벽에 부딪힘
                nx, ny = x, y
                d = (d+2)%4
            if (nx, ny) in new_grid: # 충돌
                to_remove.add((nx, ny))
            else:
                new_grid[(nx, ny)] = d
        for pos in to_remove:
            del new_grid[pos]
        grid = new_grid
    print(len(grid))