n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c, m1, m2, m3, m4, d = map(int, input().split())

p = (r-1, c-1)
lst = [p]
for i in range(m1):
    p = (p[0]-1, p[1]+1)
    lst.append(p)
for i in range(m2):
    p = (p[0]-1, p[1]-1)
    lst.append(p)
for i in range(m3):
    p = (p[0]+1, p[1]-1)
    lst.append(p)
for i in range(m4-1):
    p = (p[0]+1, p[1]+1)
    lst.append(p)
vlst = []
for i, j in lst:
    vlst.append(grid[i][j])
if d:
    vlst = vlst[1:]+[vlst[0]]
else:
    vlst = [vlst[-1]]+vlst[:-1]
for index, v in zip(lst, vlst):
    i, j = index
    grid[i][j] = v
for i in range(n):
    print(*grid[i])