n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins = sorted(coins, reverse=True)
cnt = 0
for coin in coins:
    cnt += k//coin
    k %= coin
    if k == 0:
        break
print(cnt)