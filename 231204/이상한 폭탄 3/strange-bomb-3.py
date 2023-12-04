n, k = map(int, input().split())
bombs = []
for _ in range(n):
    bombs.append(int(input()))
explode = []
for i in range(n):
    s, e = i-k, i+k
    if s < 0:
        s = 0
    if e > n-1:
        e = n-1
    cnt = bombs[s:i].count(bombs[i])+bombs[i+1:e+1].count(bombs[i])
    explode.append((cnt, bombs[i]))
explode = sorted(explode, reverse=True)
print(explode[0][1]) if explode[0][0] != 0 else print(0)