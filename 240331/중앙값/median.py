import sys
import copy
from heapq import heappush, heappop
input = sys.stdin.readline

def print_median(min_pq, i):
    tmp = copy.deepcopy(min_pq)
    for _ in range(i//2):
        heappop(tmp)
    print(tmp[0], end=' ')
    


t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    min_pq = []
    for i, elem in enumerate(arr):
        heappush(min_pq, elem)
        if i%2 == 0:
            print_median(min_pq, i)
    print()