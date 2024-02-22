def count_orders(n, cows):
    cows.sort()
    result = 0
    for x in range(n):
        for y in range(x + 1, n):
            for z in range(y + 1, n):
                if cows[y] - cows[x] <= cows[z] - cows[y] <= 2 * (cows[y] - cows[x]):
                    result += 1
    return result

n = int(input().strip())
cows = [int(input().strip()) for _ in range(n)]
print(count_orders(n, cows))