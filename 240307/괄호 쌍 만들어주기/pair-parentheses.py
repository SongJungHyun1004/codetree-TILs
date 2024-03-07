a = list(input())
n = len(a)
R = [0]*(n)
for i in range(n-2, -1, -1):
    string = ''.join(a[i:i+2])
    R[i] = R[i+1]
    if '))' == string:
        R[i] += 1
pair = 0
for i in range(n-1):
    string = ''.join(a[i:i+2])
    if '((' == string:
        pair += R[i]
print(pair)