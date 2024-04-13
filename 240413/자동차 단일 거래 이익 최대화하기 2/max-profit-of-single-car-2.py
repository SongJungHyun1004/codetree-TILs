n = int(input())
price = list(map(int, input().split()))
mx = 0
min_price = price[0]
for p in price[1:]:
    mx = max(mx, p-min_price)
    min_price = min(min_price, p)
print(mx)