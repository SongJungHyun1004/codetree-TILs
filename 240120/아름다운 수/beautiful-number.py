n = int(input())
num = []
cnt = 0

def isBeauty(num):
    number = ''.join(list(map(str, num)))
    for nn in range(1, 5):
        while True:
            idx = number.find(str(nn)*nn)
            if idx == -1:
                break
            number = number[:idx] + '0'*nn + number[idx+nn:]
    if int(number):
        return False
    else:
        return True
def choose(i):
    global cnt
    if i > n:
        if isBeauty(num):
            cnt += 1
        return
    for nn in range(1, 5):
        num.append(nn)
        choose(i+1)
        num.pop()

choose(1)
print(cnt)