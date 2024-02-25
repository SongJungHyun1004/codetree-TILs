n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [False]*n
cost = []
mn = float('inf')
def choose(i, last):
    global mn
    if i == n-1:
        mn = min(mn, sum(cost)+grid[last][0])
        return
    for j in range(1, n):
        if last == j or not grid[last][j] or visited[j]:
            continue
        cost.append(grid[last][j])
        visited[j] = True
        choose(i+1, j)
        cost.pop()
        visited[j] = False

choose(0, 0)
print(mn)