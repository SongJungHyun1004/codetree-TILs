n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst = lst[::-1]
flag = 1
while flag and lst:
    pre = lst[0]
    cnt = 1
    i = 1
    flag = 0
    while i < len(lst):
        if pre == lst[i]:
            cnt += 1
        else:
            pre = lst[i]
            if cnt >= m:
                flag = 1
                for _ in range(cnt):
                    lst.pop(i-cnt)
            cnt = 1
        i += 1
    if cnt >= m:
        flag = 1
        for _ in range(cnt):
            lst.pop(i-cnt)

print(len(lst))
for i in lst[::-1]:
    print(i)