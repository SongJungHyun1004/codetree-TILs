MAX = 100000
n = int(input())
ans = n
for i in range(MAX+1):
    rem = n-5*i
    if rem >= 0 and rem%2==0:
        ans = min(ans, i+rem//2)
if ans == n:
    print(-1)
else:
    print(ans)