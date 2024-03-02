from collections import Counter
n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
cnt_dic = Counter(lst)
cnt_dic = sorted(cnt_dic.items())
for key, value in cnt_dic:
    print(key, value)