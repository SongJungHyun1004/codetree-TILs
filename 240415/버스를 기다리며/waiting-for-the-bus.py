n, m, c = map(int, input().split())
arrive = sorted(list(map(int, input().split())))

def isPossible(mid):
    bus = 1
    pre = arrive[0]
    people = 1
    for t in arrive[1:]:
        if mid >= t-pre and people+1 <= c:
            people += 1
        else:
            pre = t
            people = 1
            bus += 1
    return bus <= m

def binary_search():
    left = 0
    right = 10**9
    mn = right
    while left <= right:
        mid = (left+right)//2
        if isPossible(mid):
            mn = min(mn, mid)
            right = mid - 1
        else:
            left = mid + 1
    return mn

print(binary_search())