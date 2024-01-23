n, m = map(int, input().split())
dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))
arr = []
mn = float('inf')

def get_dist(arr):
    mx = 0
    for i in range(m):
        for j in range(i+1, m):
            dot1 = dots[arr[i]]
            dot2 = dots[arr[j]]
            d = abs(dot1[0]-dot2[0])**2+abs(dot1[1]-dot2[1])**2
            mx = max(mx, d)
    return mx

def combi(idx, cnt):
    global mn
    if cnt == m:
        dist = get_dist(arr)
        mn = min(mn, dist)
        return
    if idx == n:
        return
    arr.append(idx)
    combi(idx+1, cnt+1)
    arr.pop()
    combi(idx+1, cnt)

combi(0, 0)
print(mn)