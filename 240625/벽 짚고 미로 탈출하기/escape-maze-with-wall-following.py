n = int(input())
x, y = map(int, input().split())
x-=1; y-=1
maze = [
    list(input())
    for _ in range(n)
]
visited = [[[False]*4 for _ in range(n)] for _ in range(n)]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(i, j):
    return 0<=i<n and 0<=j<n

def simulate(x, y, d):
    t = 0
    while in_range(x, y):
        if visited[x][y][d]:
            return -1
        visited[x][y][d] = True
        right_x, right_y = x+dxs[(d+1)%4], y+dys[(d+1)%4]
        fwd_x, fwd_y = x+dxs[d], y+dys[d]
        if maze[right_x][right_y] == '#':
            if in_range(fwd_x, fwd_y):
                if maze[fwd_x][fwd_y] == '#':
                    d = (d-1)%4
                else:
                    x, y = fwd_x, fwd_y
                    t += 1
            else:
                t += 1
                break
        else:
            d = (d+1)%4
            x, y = x+dxs[d], y+dys[d]
            t += 1
        
    return t

ans = simulate(x, y, 0)
print(ans)