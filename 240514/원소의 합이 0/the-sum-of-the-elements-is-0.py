n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
cnt = 0
dic = {}
for i in range(n):
    for j in range(n):
        if A[i]+B[j] in dic:
            dic[A[i]+B[j]] += 1
        else:
            dic[A[i]+B[j]] = 1

for i in range(n):
    for j in range(n):
        if -(C[i]+D[j]) in dic:
            cnt += dic[-(C[i]+D[j])]

print(cnt)