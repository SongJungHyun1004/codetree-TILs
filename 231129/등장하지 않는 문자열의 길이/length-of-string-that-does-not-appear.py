n = int(input())
s = input()
def myCount(tmp, length):
    cnt = 0
    for i in range(n-length+1):
        if s[i:i+length] == tmp:
            cnt += 1
    return cnt
for i in range(1, n+1):
    flag = 1
    for j in range(n-i+1):
        if myCount(s[j:j+i], i) > 1:
            flag = 0
            break
    if flag:
        print(i)
        exit(0)