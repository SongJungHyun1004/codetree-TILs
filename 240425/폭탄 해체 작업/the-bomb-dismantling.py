n = int(input())
lst = []
for _ in range(n):
    score, time = map(int, input().split())
    lst.append((score, time))
lst.sort(key = lambda x: (x[1], -x[0]))
ans = 0
last_t = 0
for s, t in lst:
    if t > last_t:
        ans += s
        last_t = t
print(ans)