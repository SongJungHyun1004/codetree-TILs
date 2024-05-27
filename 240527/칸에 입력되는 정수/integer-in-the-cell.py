import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
visited = {}
cnt = 0
for _ in range(m):
    k = int(input())
    if k not in visited:
        cnt += 1
        visited[k] = 1
print(cnt)