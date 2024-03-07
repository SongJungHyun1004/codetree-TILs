n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

prefix = [0]*(n+1)
first_occurrence = [-1]*7
first_occurrence[0] = 0
mx = 0

for i in range(1, n+1):
    prefix[i] = (prefix[i-1]+arr[i])%7
    if first_occurrence[prefix[i]] == -1:
        first_occurrence[prefix[i]] = i
    else:
        mx = max(mx, i - first_occurrence[prefix[i]])

print(mx)