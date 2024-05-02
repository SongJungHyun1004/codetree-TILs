n = int(input())
string = input()
L = [0]*n # C 개수
R = [0]*n # W 개수
if string[0] == 'C':
    L[0] = 1
if string[-1] == 'W':
    R[-1] = 1

for i in range(1, n):
    L[i] = L[i-1]+1 if string[i] == 'C' else L[i-1]
for i in range(n-2, -1, -1):
    R[i] = R[i+1]+1 if string[i] == 'W' else R[i+1]

cnt = 0
for i in range(1, n-1):
    if string[i] == 'O':
        cnt += L[i-1]*R[i+1]
print(cnt)