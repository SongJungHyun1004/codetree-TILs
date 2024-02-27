n = int(input())
grid = [
    [0]*201
    for _ in range(201)
]
color = 0 # red:0, blue:1
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1+=100;y1+=100; x2+=100;y2+=100
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = color
    color = 1 - color
area = 0
for i in range(201):
    for j in range(201):
        area += grid[i][j]
print(area)