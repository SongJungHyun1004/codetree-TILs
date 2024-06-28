import sys
sys.setrecursionlimit(10**5)
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False]*n for _ in range(n)]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def dfs(x, y):
    global people
    people += 1
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny]:
            dfs(nx, ny)

people_lst = []
for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            people = 0
            dfs(i, j)
            people_lst.append(people)
people_lst.sort()
print(len(people_lst))
for i in people_lst:
    print(i)