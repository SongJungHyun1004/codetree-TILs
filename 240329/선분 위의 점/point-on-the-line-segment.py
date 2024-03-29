n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def lower_bound(target):
    left = 0
    right = n-1
    mn = n
    while left <= right:
        mid = (left+right)//2
        if arr[mid] >= target:
            right = mid - 1
            mn = min(mn, mid)
        else:
            left = mid + 1
    return mn
            
def upper_bound(target):
    left = 0
    right = n-1
    mn = n
    while left <= right:
        mid = (left+right)//2
        if arr[mid] > target:
            right = mid - 1
            mn = min(mn, mid)
        else:
            left = mid + 1
    return mn

for _ in range(m):
    s, e = map(int, input().split())
    print(upper_bound(e) - lower_bound(s))