n = int(input())
arr = list(map(int, input().split()))
count = [0]*100001
j = 0
mx = 0
for i in range(n):
    while j < n and count[arr[j]] == 0:
        count[arr[j]] += 1
        j += 1
    mx = max(mx, j-i)
    count[arr[i]] -= 1
print(mx)