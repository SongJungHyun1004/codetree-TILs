n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

def is_possible(k):
    cnt = 0
    for elem in lst:
        cnt += elem//k
    return cnt >= m

def binary_search():
    left = 1
    right = 10000
    mx = 0
    while left <= right:
        mid = (left+right)//2
        if is_possible(mid):
            left = mid+1
            mx = max(mx, mid)
        else:
            right = mid-1
    return mx

print(binary_search())