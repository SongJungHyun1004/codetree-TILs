import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
dic = {}
for elem in arr:
    if k-elem in dic:
        cnt += dic[k-elem]
    if elem in dic:
        dic[elem] += 1
    else:
        dic[elem] = 1
print(cnt)