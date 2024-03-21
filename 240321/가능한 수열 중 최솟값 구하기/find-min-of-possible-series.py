n = int(input())
num = []

def choose(i):
    if i == n:
        print(''.join(map(str, num)))
        exit(0)
    for nn in range(4, 7):
        if num:
            if num[-1] == nn:
                continue
            num_len = 3
            ii = 1
            flag = 1
            while len(num) >= num_len:
                if num[-num_len:-num_len+(num_len+1)//2] == num[-ii:]+[nn]:
                    flag = 0
                    break
                num_len += 2
                ii += 1
            if flag:
                num.append(nn)
                choose(i+1)
                num.pop()
            else:
                continue
        else:
            num.append(nn)
            choose(i+1)
            num.pop()
choose(0)