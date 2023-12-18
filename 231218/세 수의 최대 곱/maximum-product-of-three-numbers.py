n = int(input())
arr = sorted(list(map(int, input().split())))
print(max(arr[0]*arr[1]*arr[-1], arr[-1]*arr[-2]*arr[-3]))