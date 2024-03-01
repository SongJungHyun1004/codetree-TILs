s = int(input())

def binary_search(s):
    left = 1
    right = s
    mx = 0
    while left <= right:
        mid = (left+right)//2
        if (mid*(mid+1))//2 <= s:
            left = mid+1
            mx = max(mx, mid)
        else:
            right = mid-1
    return mx
print(binary_search(s))