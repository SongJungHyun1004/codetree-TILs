n = int(input())
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))
mx = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = lst[i]
            x2, y2 = lst[j]
            x3, y3 = lst[k]
            if (x1 != x2 and x2 != x3 and x1 != x3) or (y1 != y2 and y2 != y3 and y1 != y3):
                continue
            s = abs((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3))
            mx = max(mx, s)
print(mx) if mx != -1 else print(0)