n = int(input())

def count(mid):
    cal = mid//3+mid//5-mid//15
    return mid-cal

def binary_search():
    left = 1
    right = 10**10
    mn = right
    while left <= right:
        mid = (left+right)//2
        if count(mid) >= n:
            mn = min(mn, mid)
            right = mid - 1
        else:    
            left = mid + 1
    return mn
print(binary_search())