n, m, t = map(int, input().split())
direction = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3,
}
dx = [0,1,0,-1]
dy = [1,0,-1,0]
objects = {}
for num in range(1, m+1):
    r, c, d, w = input().split()
    r = int(r)-1; c = int(c)-1; w = int(w)
    objects[(r, c)] = [num, direction[d], w]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

for _ in range(t):
    new_objects = {}
    for (x, y), info in objects.items():
        num, d, w = info[0], info[1], info[2]
        nx, ny = x + dx[d], y + dy[d]
        if not in_range(nx, ny):
            nx, ny = x, y
            d = (d+2)%4
        if (nx, ny) in new_objects:
            if new_objects[(nx, ny)][0] > num:
                num = new_objects[(nx, ny)][0]
                d = new_objects[(nx, ny)][1]
            new_objects[(nx, ny)] = [num, d, new_objects[(nx, ny)][2] + w]
        else:
            new_objects[(nx, ny)] = [num, d, w]
    objects = new_objects

mx = 0
for _, info in objects.items():
    mx = max(mx, info[2])
print(len(objects), mx)