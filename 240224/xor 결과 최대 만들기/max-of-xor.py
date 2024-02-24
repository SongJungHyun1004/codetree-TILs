n, m = map(int, input().split())
arr = list(map(int, input().split()))
selected = [False]*n
num = []

def xor(num):
    result = num[0]
    for i in range(1, len(num)):
        result ^= num[i]
    return result
def combi(idx, last):
    global mx
    if idx == m:
        mx = max(mx, xor(num))
        return
    for i in range(last, n):
        num.append(arr[i])
        selected[i] = True
        combi(idx+1, last)
        num.pop()
        selected[i] = False
mx = 0
combi(0, 0)
print(mx)