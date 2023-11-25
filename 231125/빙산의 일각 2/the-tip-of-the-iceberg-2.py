n = int(input())
h = [0]*n
for i in range(n):
    h[i] = int(input())
mx = float('-inf')

def get_cnt(tmp):
    cnt = 0
    for i in range(n-1):
        if tmp[i] and not tmp[i+1]:
            cnt += 1
    cnt += 1
    if not tmp[n-1]:
        cnt -= 1
    return cnt

for height in range(1, max(h)):
    tmp = [h[i]-height if h[i] > height else 0 for i in range(n)]
    mx = max(mx, get_cnt(tmp))
print(mx)