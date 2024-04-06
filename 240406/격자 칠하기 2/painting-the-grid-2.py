import sys
sys.setrecursionlimit(10**5)
from collections import deque
import math
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False]*n for _ in range(n)]
half = math.floor(n**2/2+0.5)
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def dfs(x, y, mid):
    if visited[x][y]:
        return 0
    size = 1
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and abs(grid[nx][ny]-grid[x][y]) <= mid:
            size += dfs(nx, ny, mid)
    return size

def isPossible(mid):
    global size
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if half <= dfs(i, j, mid):
                    return True
    return False

def binary_search():
    left = 0
    right = 10**6
    d = 0
    while left <= right:
        mid = (left+right)//2
        if isPossible(mid):
            right = mid - 1
            d = mid
        else:
            left = mid + 1
    return d

print(binary_search())