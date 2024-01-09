n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
def get_coin(row, col):
    coin = 0
    for i in range(row, row+3):
        for j in range(col, col+3):
            coin += grid[i][j]
    return coin
mx = 0
for i in range(n-2):
    for j in range(n-2):
        num = get_coin(i, j)
        mx = max(mx, num)
print(mx)