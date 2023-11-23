x, y = map(int, input().split())
mx = float('-inf')
for i in range(x, y+1):
    lst = list(map(int, str(i)))
    mx = max(mx, sum(lst))
print(mx)