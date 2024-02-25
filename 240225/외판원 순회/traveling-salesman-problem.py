n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [False]*n
cost = []
mn = float('inf')
def choose(i):
    global mn
    if i == n:
        mn = min(mn, sum(cost))
        return
    for j in range(n):
        if i == j or visited[j]:
            continue
        cost.append(grid[i][j])
        visited[j] = True
        choose(i+1)
        cost.pop()
        visited[j] = False

choose(0)
print(mn)