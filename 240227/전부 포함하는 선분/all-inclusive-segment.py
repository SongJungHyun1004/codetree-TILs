n = int(input())
lst = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    lst.append((x1, x2))
tmp = lst[:]
tmp = sorted(tmp)
tmp.pop(0)
a = tmp[0][0]
tmp = sorted(tmp, key=lambda x:x[1])
b = tmp[-1][1]
ans1= b-a

tmp2 = lst[:]
tmp2 = sorted(tmp2, key=lambda x:x[1])
tmp2.pop()
b = tmp2[-1][1]
tmp2 = sorted(tmp2)
a = tmp2[0][0]
ans2 = b-a

print(min(ans1, ans2))