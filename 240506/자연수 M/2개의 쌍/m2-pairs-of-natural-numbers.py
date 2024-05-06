import sys
input = sys.stdin.readline
lst = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    lst += [y]*x
lst.sort()
m = len(lst)
print(min(lst[0]+lst[-1], lst[m//2-1]+lst[m//2]))