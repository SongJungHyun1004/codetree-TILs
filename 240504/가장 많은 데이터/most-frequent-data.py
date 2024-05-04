import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
count = Counter(lst)
print(sorted(count.values())[-1])