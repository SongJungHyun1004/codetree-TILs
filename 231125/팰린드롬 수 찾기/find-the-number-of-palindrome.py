x, y = map(int, input().split())
def is_palindrome(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[len(n)-1-i]:
            return False
    return True
cnt = 0
for i in range(x, y+1):
    if is_palindrome(i):
        cnt += 1
print(cnt)