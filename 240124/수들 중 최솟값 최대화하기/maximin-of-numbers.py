import sys
input = sys.stdin.readline
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
row_visited = [False]*n
col_visited = [False]*n
pos_lst = []
mx = 0

def get_min(pos_lst):
    mn = float('inf')
    for x, y in pos_lst:
        mn = min(mn, grid[x][y])
    return mn

def combi(i):
    global mx
    if i == n:
        mx = max(mx, get_min(pos_lst))
        return
    for x in range(n):
        if row_visited[x]:
            continue
        for y in range(n):
            if col_visited[y]:
                continue
            pos_lst.append((x, y))
            row_visited[x] = True
            col_visited[y] = True
            combi(i+1)
            pos_lst.pop()
            row_visited[x] = False
            col_visited[y] = False
            
combi(0)
print(mx)