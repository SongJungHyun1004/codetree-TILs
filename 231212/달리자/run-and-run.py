n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dist = 0
for i in range(n-1):
    if a[i] > b[i]:
        people = a[i]-b[i]
        a[i+1] += people
        dist += people
print(dist)