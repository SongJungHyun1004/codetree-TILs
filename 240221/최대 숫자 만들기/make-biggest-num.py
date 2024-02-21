from functools import cmp_to_key
n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

def compare(x, y):
    if x[0] > y[0]:
        return -1
    elif x[0] < y[0]:
        return 1
    else:
        if x+y > y+x:
            return -1
        else:
            return 1

arr = sorted(arr, key=cmp_to_key(compare))
print(''.join(arr))