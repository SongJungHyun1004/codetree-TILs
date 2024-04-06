from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, tmax = map(int, input().split())
during = []
for _ in range(n):
    d = int(input())
    during.append(d)

def isPossible(mid):
    time = 0
    stage = []
    for i in range(mid):
        heappush(stage, during[i])
    for i in range(mid, n):
        time = heappop(stage)
        heappush(stage, time + during[i])
    while stage:
        time = heappop(stage)
    return time <= tmax


def binary_search():
    left = 0
    right = n
    k = right
    while left <= right:
        mid = (left+right)//2
        if isPossible(mid):
            right = mid - 1
            k = min(k, mid)
        else:
            left = mid + 1
    return k

print(binary_search())