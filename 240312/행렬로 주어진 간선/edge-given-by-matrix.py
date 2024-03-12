import sys
input = sys.stdin.readline
n = int(input())
path = [
    list(map(int, input().split()))
    for _ in range(n)
]
for i in range(n):
    path[i][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if path[i][k] and path[k][j]:
                path[i][j] = 1

for i in range(n):
    print(*path[i])