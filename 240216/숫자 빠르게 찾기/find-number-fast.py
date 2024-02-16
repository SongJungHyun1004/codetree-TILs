n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid+1
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
for _ in range(m):
    print(binary_search(int(input())))