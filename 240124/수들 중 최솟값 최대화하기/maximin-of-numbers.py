import sys
input = sys.stdin.readline
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [False]*n
pos_lst = []
mx = -1

def get_min(pos_lst):
    mn = float('inf')
    for x, y in pos_lst:
        mn = min(mn, grid[x][y])
    return mn

def combi(i):
    global mx
    if i == n:
        mn = float('inf')
        for j in range(n):
            mn = min(mn, grid[j][pos_lst[j]])
        mx = max(mx, mn)
        return
    for j in range(n):
        if visited[j]:
            continue
        visited[j] = True
        pos_lst.append(j)
        combi(i+1)
        visited[j] = False
        pos_lst.pop()

combi(0)
print(mx)