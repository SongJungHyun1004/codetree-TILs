n = int(input())
dic = {}
for _ in range(n):
    x, y = map(int, input().split())
    if x in dic:
        if y < dic[x]:
            dic[x] = y
    else:
        dic[x] = y
print(sum(dic.values()))