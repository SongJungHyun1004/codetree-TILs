n = int(input())
MAX = 100
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))
mn = float('inf')
for i in range(2, MAX+1, 2):
    for j in range(2, MAX+1, 2):
        area = [0]*4
        for p in lst:
            x, y = p
            if x < i and y < j:
                area[0] += 1
            elif x > i and y < j:
                area[1] += 1
            elif x < i and y > j:
                area[2] += 1
            elif x > i and y > j:
                area[3] += 1
        mn = min(mn, max(area))
print(mn)