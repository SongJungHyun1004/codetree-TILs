import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

group1 = defaultdict(int)
cnt = 0

for i in range(n):
    for j in range(n):
        s = a[i] + b[j]
        group1[s] += 1

for i in range(n):
    for j in range(n):
        s2 = -(c[i] + d[j])  # c+d의 합의 음수 값을 직접 계산
        if s2 in group1:  # group1에 s2의 음수 값이 존재하는지 확인
            cnt += group1[s2]  # 존재한다면, 그 조합의 수만큼 cnt를 증가

print(cnt)