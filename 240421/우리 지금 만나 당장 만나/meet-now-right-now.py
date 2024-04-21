import math

n = int(input())
positions = list(map(int, input().split()))
speeds = list(map(int, input().split()))

def can_meet(mid):
    left_most = -math.inf
    right_most = math.inf
    for position, speed in zip(positions, speeds):
        left_most = max(left_most, position - mid * speed)
        right_most = min(right_most, position + mid * speed)
    return left_most <= right_most

def binary_search():
    left = 0
    right = 1e9  # 최대 가능 거리
    while right - left > 1e-6:  # 정밀도 조정
        mid = (left + right) / 2
        if can_meet(mid):
            right = mid
        else:
            left = mid
    return right

print(f'{binary_search():.4f}')