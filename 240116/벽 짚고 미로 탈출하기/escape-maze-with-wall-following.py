n = int(input())
x, y = map(int, input().split())
miro = [
    list(input())
    for _ in range(n)
]
x-=1;y-=1
dx = [0,-1,0,1]
dy = [1,0,-1,0]
d = 0
t = 0
lst = []
def in_range(x, y):
    return 0<=x<n and 0<=y<n

while True:
    lst.append((x, y))
    nx, ny = x + dx[d], y + dy[d]
    if in_range(nx, ny):
        if miro[nx][ny] == '#':
            d += 1
        else:
            if miro[nx][ny] != '#':
                d -= 1
            x, y = nx, ny
            t += 1
            if (x, y) in lst:
                break
    else:
        print(t+1)
        exit(0)
print(-1)