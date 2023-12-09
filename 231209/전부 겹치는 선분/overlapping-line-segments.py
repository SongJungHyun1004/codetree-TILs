n = int(input())
line = [0]*101
for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1, x2+1):
        line[i] += 1
print("Yes") if n in line else print("No")