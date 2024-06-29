n, m = map(int, input().split())
arr = list(map(int, input().split()))

num = []
def choose(i, cnt, value):
    global mx
    if i == n:
        if cnt == m:
            mx = max(mx, value)
            return
        return
    choose(i+1, cnt+1, value^arr[i])
    choose(i+1, cnt, value)
mx = 0
choose(0, 0, 0)
print(mx)