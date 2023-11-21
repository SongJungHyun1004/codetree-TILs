n, k = map(int, input().split())
bombs = []
for _ in range(n):
    bombs.append(int(input()))
lst = []
for i in range(n):
    left, right = i-k, i+k
    if left < 0:
        left = 0
    if right > n-1:
        right = n-1
    if bombs[i] in bombs[left:i] or bombs[i] in bombs[i+1:right]:
        lst.append(bombs[i])
print(max(lst)) if lst else print(-1)