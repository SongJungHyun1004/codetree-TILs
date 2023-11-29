n = int(input())
s = input()

for i in range(1, n+1):
    flag = 1
    for j in range(n-i):
        if s.count(s[j:j+i]) > 1:
            flag = 0
            break
    if flag:
        print(i)
        exit(0)