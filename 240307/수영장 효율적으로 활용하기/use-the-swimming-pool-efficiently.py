n, m = map(int, input().split())
using_time = list(map(int, input().split()))

def is_possible(t):
    lane = 1
    cur_lane_total = 0
    for time in using_time:
        if cur_lane_total + time > t:
            cur_lane_total = time
            lane += 1
        else:
            cur_lane_total += time
    return lane <= m
        
def binary_search():
    left = max(using_time)
    right = sum(using_time)
    mn = right
    while left <= right:
        mid = (left+right)//2
        if is_possible(mid):
            right = mid - 1
            mn = min(mn, mid)
        else:
            left = mid + 1
    return mn

print(binary_search())