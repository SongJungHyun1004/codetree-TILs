n, m = map(int, input().split())
arr = list(map(int, input().split()))
def upper_bound(target):
    left = 0
    right = n-1
    min_idx = n
    while left <= right:
        mid = (left+right)//2
        if arr[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx
def lower_bound(target):
    left = 0
    right = n-1
    min_idx = n
    while left <= right:
        mid = (left+right)//2
        if arr[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx
for _ in range(m):
    num = int(input())
    print(upper_bound(num)-lower_bound(num))