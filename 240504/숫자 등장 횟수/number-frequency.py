import sys
input = sys.stdin.readline
from collections import Counter

n, m = map(int, input().split())
arr = list(map(int, input().split()))
count = Counter(arr)
m_list = list(map(int, input().split()))
for k in m_list:
    if k in count:
        print(count[k], end=' ')
    else:
        print(0, end=' ')