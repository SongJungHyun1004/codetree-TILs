import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
grid = [
    [0]*n
    for _ in range(n)
]
for _ in range(m):
    x, y = map(int, input().split())
    x-=1;y-=1
    grid[x][y] = 1

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
direction = {
    'R':0,
    'D':1,
    'L':2,
    'U':3,
}
def in_range(x, y):
    return 0<=x<n and 0<=y<n

t = 0
head = (0, 0)
body = []
for _ in range(k):
    d, p = input().split()
    p = int(p)
    x, y = head
    flag = 0
    for i in range(1, p+1):
        t += 1
        nx, ny = x + dxs[direction[d]]*i, y + dys[direction[d]]*i
        if in_range(nx, ny):
            body.insert(0, head)
            head = (nx, ny)
            if grid[nx][ny]:
                grid[nx][ny] = 0
            else:
                body.pop()
            if head in body:
                flag = 1
                break
        else:
            flag = 1
            break
    if flag:
        break
print(t)