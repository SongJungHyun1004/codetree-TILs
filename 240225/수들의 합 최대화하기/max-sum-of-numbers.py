n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
num = []
selected_j = [False]*n
mx = 0
def choose(i):
    global mx
    if i == n:
        mx = max(mx, sum(num))
        return
    for j in range(n):
        if not selected_j[j]:
            num.append(grid[i][j])
            selected_j[j] = True
            choose(i+1)
            num.pop()
            selected_j[j] = False
choose(0)
print(mx)