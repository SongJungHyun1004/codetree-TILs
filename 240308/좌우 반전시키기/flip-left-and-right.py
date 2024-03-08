n = int(input())
switch = list(map(int, input().split()))
pre = switch[0]
cnt = 0
if n == 1:
    if switch[0]:
        print(cnt)
    else:
        print(-1)
    exit(0)

for i in range(1, n-1):
    if not pre:
        switch[i-1] = 1
        switch[i] = 1-switch[i]
        switch[i+1] = 1-switch[i+1]
        cnt += 1
    pre = switch[i]
if switch[-1] == switch[-2]:
    if switch[-1]:
        print(cnt)
    else:
        print(cnt+1)
else:
    print(-1)