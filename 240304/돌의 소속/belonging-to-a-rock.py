n, q = map(int, input().split())
group = [
    [0]*(n+1)
    for _ in range(3)
]
for i in range(1, n+1):
    g = int(input())-1
    group[g][i] = 1
prefix = [
    [0]*(n+1)
    for _ in range(3)
]
for i in range(3):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i][j-1] + group[i][j]

for _ in range(q):
    a, b = map(int, input().split())
    ans = []
    for i in range(3):
        ans.append(prefix[i][b]-prefix[i][a-1])
    print(*ans)