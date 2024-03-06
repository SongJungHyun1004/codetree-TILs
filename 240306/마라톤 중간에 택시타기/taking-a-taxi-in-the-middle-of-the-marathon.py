n = int(input())
check_point = []
for _ in range(n):
    x, y = map(int, input().split())
    check_point.append((x, y))

def get_dist(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1-x2)+abs(y1-y2)

L = [0]*n
R = [0]*n
for i in range(1, n):
    L[i] = L[i-1] + get_dist(check_point[i-1], check_point[i])
for i in range(n-2, -1, -1):
    R[i] = R[i+1] + get_dist(check_point[i+1], check_point[i])

mn_dist = float('inf')
for skip in range(1, n-1):
    dist = L[skip-1]+R[skip+1]+get_dist(check_point[skip-1], check_point[skip+1])
    mn_dist = min(mn_dist, dist)

print(mn_dist)