import copy
n, b = map(int, input().split())
prices = []
for _ in range(n):
    p, s = map(int, input().split())
    prices.append([p, s])
ans = 0
for i in range(n):
    tmp = copy.deepcopy(prices)
    tmp[i][0] /= 2
    lst = [tmp[a][0]+tmp[a][1] for a in range(n)]
    lst.sort()
    
    student = 0
    total = 0
    for j in range(n):
        if total + lst[j] > b:
            break
        total += lst[j]
        student += 1
    ans = max(ans, student)
print(ans)