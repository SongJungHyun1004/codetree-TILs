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
    temp = []
    while i < len(lst):
        if pre == lst[i]:
            cnt += 1
        else:
            if cnt < m:
                temp.extend([pre]*cnt)
            else:
                flag = 1
            pre = lst[i]
            cnt = 1
        i += 1
    if cnt < m:
        temp.extend([pre]*cnt)
    else:
        flag = 1
    lst = temp

print(len(lst))
for i in lst[::-1]:
    print(i)