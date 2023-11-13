n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
def check_diff(i, j, k):
    if min(abs(a1-i), n-abs(a1-i)) <=2 and min(abs(b1-j), n-abs(b1-j)) <=2 and min(abs(c1-k), n-abs(c1-k)) <=2:
        return True
    if min(abs(a2-i), n-abs(a2-i)) <=2 and min(abs(b2-j), n-abs(b2-j)) <=2 and min(abs(c2-k), n-abs(c2-k)) <=2:
        return True
    return False
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if check_diff(i, j, k):
                cnt += 1
print(cnt)