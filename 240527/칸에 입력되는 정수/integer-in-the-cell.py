import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
visited = {}
cnt = 0
for _ in range(m):
    k = int(input())
    noMore = True
    for i in range(k, 0, -1):
        if i not in visited:
            cnt += 1
            visited[i] = 1
            noMore = False
            break
    if noMore:
        break
print(cnt)