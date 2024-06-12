n, m = map(int, input().split())
arr = list(map(int, input().split()))

mx = 0
def combi(i, cnt, val):
    global mx
    if i == n:
        if cnt == m:
            mx = max(mx, val)
        return
    combi(i+1, cnt+1, val^arr[i])
    combi(i+1, cnt, val)
combi(0, 0, 0)
print(mx)