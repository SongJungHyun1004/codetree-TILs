n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
def is_sub():
    i, j = 0, 0
    for i in range(m):
        while j < n and B[i] != A[j]:
            j += 1
        if j == n:
            return False
    return True
print('Yes') if is_sub() else print('No')