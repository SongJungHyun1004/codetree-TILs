n = int(input())
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append((s, +1))
    lst.append((e, -1))
lst = sorted(lst)

cnt = 0
length = 0
for i, (p, v) in enumerate(lst):
    if cnt >= 1:
        pre_p, _ = lst[i-1]
        length += p - pre_p
    cnt += v
print(length)