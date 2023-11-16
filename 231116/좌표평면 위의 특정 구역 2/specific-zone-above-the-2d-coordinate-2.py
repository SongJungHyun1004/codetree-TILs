n = int(input())
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))
mn_area = float('inf')
for i in range(n):
    mx_x, mx_y = float('-inf'), float('-inf')
    mn_x, mn_y = float('inf'), float('inf')
    for j in range(n):
        if i == j:
            continue
        x, y = lst[j]
        mx_x, mx_y = max(mx_x, x), max(mx_y, y)
        mn_x, mn_y = min(mn_x, x), min(mn_y, y)
    area = (mx_x-mn_x)*(mx_y-mn_y)
    mn_area = min(mn_area, area)
print(mn_area)