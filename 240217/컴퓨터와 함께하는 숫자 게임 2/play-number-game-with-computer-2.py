m = int(input())
a, b = map(int, input().split())
mn = float('inf')
mx = 0

def binary_search(target):
    left = 1
    right = m
    turn = 1
    while left <= right:
        mid = (left+right)//2
        if mid == target:
            return turn
        if mid > target:
            right = mid - 1
        else:
            left = mid + 1
        turn += 1
for i in range(a, b+1):
    v = binary_search(i)
    mn = min(mn, v)
    mx = max(mx, v)
print(mn, mx)