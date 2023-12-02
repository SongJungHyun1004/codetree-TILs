n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(val):
    indexs = []
    for i, elem in enumerate(arr):
        if elem <= val:
            indexs.append(i)
    if len(indexs) == 1:
        return False
    for i in range(1, len(indexs)):
        dist = indexs[i] - indexs[i-1]
        if dist > k:
            return False
    return True

mn = float('inf')
for a in range(max(arr[0], arr[-1]), max(arr)+1):
    if is_possible(a):
        mn = min(mn, a)
print(mn)