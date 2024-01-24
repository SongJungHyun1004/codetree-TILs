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
mx = -1

def get_min(pos_lst):
    mn = float('inf')
    for x, y in pos_lst:
        mn = min(mn, grid[x][y])
    return mn

def combi(i, curr_min):
    global mx
    if curr_min <= mx:  # Pruning
        return
    if i == n:
        mx = max(mx, curr_min)
        return
    for x in range(n):
        if row_visited[x]:
            continue
        for y in range(n):
            if col_visited[y]:
                continue
            row_visited[x] = True
            col_visited[y] = True
            pos_lst.append((x, y))
            combi(i+1, min(curr_min, grid[x][y]))  # Update current minimum
            row_visited[x] = False
            col_visited[y] = False
            pos_lst.pop()

combi(0, float('inf'))
print(mx)