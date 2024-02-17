m = int(input())
a, b = map(int, input().split())
arr = [i+1 for i in range(m)]
mn = float('inf')
mx = 0

def binary_search(target):
    left = 0
    right = m-1
    turn = 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return turn
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        turn += 1
for i in range(a, b+1):
    v = binary_search(i)
    mn = min(mn, v)
    mx = max(mx, v)
print(mn, mx)