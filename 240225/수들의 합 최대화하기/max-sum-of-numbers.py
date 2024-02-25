n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
num = []
selected_i = [False]*n
selected_j = [False]*n
mx = 0
def choose(idx):
    global mx
    if idx == n:
        mx = max(mx, sum(num))
        return
    for i in range(n):
        for j in range(n):
            if not selected_i[i] and not selected_j[j]:
                num.append(grid[i][j])
                selected_i[i] = True
                selected_j[j] = True
                choose(idx+1)
                num.pop()
                selected_i[i] = False
                selected_j[j] = False
choose(0)
print(mx)