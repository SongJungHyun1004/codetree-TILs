import sys
input = sys.stdin.readline
from collections import Counter

n, k = map(int, input().split())
count_dic = Counter(list(map(int, input().split())))
lst = sorted(count_dic.items(), key=lambda x:(-x[1], -x[0]))

for i in range(k):
    print(lst[i][0], end=' ')