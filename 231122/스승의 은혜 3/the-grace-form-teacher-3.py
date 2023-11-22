n, b = map(int, input().split())
prices = []
for _ in range(n):
    p, s = map(int, input().split())
    prices.append((int(p)//2, s))
prices = [(0,0)]+sorted(prices)
cnt = 0
total = 0
for i in range(1, n+1):
    total += prices[i-1][0]+prices[i][0]+prices[i][1]
    if total > b:
        break
    cnt += 1
print(cnt)