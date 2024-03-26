import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
group1 = {}
group2 = {}

for i in range(n):
    for j in range(n):
        s = a[i]+b[j]
        if s in group1:
            group1[s] += 1
        else:
            group1[s] = 1
        s2 = c[i]+d[j]
        if s2 in group2:
            group2[s2] += 1
        else:
            group2[s2] = 1
cnt = 0
for i in group1.keys():
    for j in group2.keys():
        if i + j == 0:
            cnt += group1[i]*group2[j]
print(cnt)