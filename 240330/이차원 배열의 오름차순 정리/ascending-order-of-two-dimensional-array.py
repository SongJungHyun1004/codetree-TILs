n = int(input())
k = int(input())
def count(mid):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(n, mid//i)
    return cnt



def binary_search():
    left = 1
    right = n**2
    mn = right
    while left <= right:
        mid = (left+right)//2
        if count(mid) >= k:
            right = mid - 1
            mn = min(mn, mid)
        else:
            left = mid + 1
    return mn

print(binary_search())