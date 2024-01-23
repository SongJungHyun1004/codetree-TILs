n, m = map(int, input().split())
num = []
def combi(cur_num, cnt):
    if cur_num == n+1:
        if cnt == m:
            print(*num)
        return
    num.append(cur_num)
    combi(cur_num+1, cnt+1)
    num.pop()
    combi(cur_num+1, cnt)
combi(1, 0)