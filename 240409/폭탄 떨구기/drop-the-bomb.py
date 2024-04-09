n, k = map(int, input().split())
dots = []
for _ in range(n):
    dots.append(int(input()))
dots.sort()

def isPossible(mid):
    idx = 0
    for _ in range(k):
        cover = dots[idx]+2*mid
        while dots[idx] <= cover:
            idx += 1
            if idx == n:
                return True
    return False

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