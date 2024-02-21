n = int(input())
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append((s, +1))
    lst.append((e, -1))
lst = sorted(lst)
cnt = 0
mx = 0
for _, num in lst:
    cnt += num
    mx = max(mx, cnt)
print(mx)