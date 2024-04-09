n, k = map(int, input().split())
dots = []
for _ in range(n):
    dots.append(int(input()))
dots.sort()

def isPossible(mid):
    cnt = 1
    idx = 0
    for i in range(n):
        if dots[i]-dots[idx] <= 2*mid:
            continue
        else:
            cnt += 1
            idx = i
    return cnt <= k

def binary_search():
    left = 0
    right = 10**9
    R = right
    while left <= right:
        mid = (left+right)//2
        if isPossible(mid):
            right = mid - 1
            R = min(R, mid)
        else:
            left = mid + 1
    return R
print(binary_search())