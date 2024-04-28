import sys
input = sys.stdin.readline

mapper = {
    'a':0,
    'b':1,
    'c':2,
}
n, m, k = map(int, input().split())
grid = [[[0, 0, 0] for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    string = list(input().rstrip())
    for j, s in enumerate(string, start=1):
        grid[i][j][mapper[s]] = 1

prefix = [[[0, 0, 0] for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        for kk in range(3):
            prefix[i][j][kk] = grid[i][j][kk] + prefix[i-1][j][kk] + prefix[i][j-1][kk] - prefix[i-1][j-1][kk]

for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    ans = []
    for i in range(3):
        ans.append(prefix[r2][c2][i] - prefix[r2][c1-1][i] - prefix[r1-1][c2][i] + prefix[r1-1][c1-1][i])
    print(*ans)