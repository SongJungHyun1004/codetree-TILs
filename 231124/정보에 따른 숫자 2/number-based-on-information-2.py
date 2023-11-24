t, a, b = map(int, input().split())
lst = ['']*1001
for _ in range(t):
    c, x = input().split()
    lst[int(x)] = c

def min_dist(k, c):
    r, l = 1001, 1001
    for i in range(k, 1001):
        if lst[i] == c:
            r = i-k
            break
    for i in range(k, 0, -1):
        if lst[i] == c:
            l = k-i
            break   
    return min(r, l)

cnt = 0
for k in range(a, b+1):
    d1 = min_dist(k, 'S')
    d2 = min_dist(k, 'N')
    if d1 <= d2:
        cnt += 1
print(cnt)