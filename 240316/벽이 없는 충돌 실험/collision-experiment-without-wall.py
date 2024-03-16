import sys
import copy
input = sys.stdin.readline
t = int(input())
def can_crash(m1, m2):
    x1,y1,d1 = m1
    x2,y2,d2 = m2
    if d1 == d2:
        return False
    if abs(d1-d2) == 2:
        if (d1==0 and d2==2 and x1<x2) or \
            (d1==2 and d2==0 and x1>x2) or \
            (d1==1 and d2==3 and y1>y2) or \
            (d1==3 and d2==1 and y1<y2):
            return True
    if abs(d1-d2) == 1 or abs(d1-d2) == 3:
        if (d1==0 and d2==1 and x1<x2 and y1<y2) or \
            (d1==0 and d2==3 and x1<x2 and y1>y2) or \
            (d1==1 and d2==0 and x1>x2 and y1>y2) or \
            (d1==1 and d2==2 and x1<x2 and y1>y2) or \
            (d1==2 and d2==1 and x1>x2 and y1<y2) or \
            (d1==2 and d2==3 and x1>x2 and y1>y2) or \
            (d1==3 and d2==2 and x1<x2 and y1<y2) or \
            (d1==3 and d2==0 and x1>x2 and y1<y2):
            return True
    return False

def isEnd(marbles):
    #모든 구슬이 서로 충돌할 가능성이 없으면 True
    if len(marbles) < 2:
        return True
    lst = []
    for v in marbles.values():
        x, y, _, d = v
        lst.append((x,y,d))
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            if can_crash(lst[i], lst[j]):
                return False
    return True
for _ in range(t):
    n = int(input())
    dxs = [1,0,-1,0]
    dys = [0,-1,0,1]
    direction = {
        'R':0,
        'D':1,
        'L':2,
        'U':3,
    }
    last_crash = -1
    marbles = {}
    for i in range(n):
        x, y, w, d = input().split()
        x = int(x)*2; y = int(y)*2; w = int(w); d = direction[d]
        marbles[i+1] = (x, y, w, d)
    
    sec = 0
    while True:
        new_marbles = {}
        new_pos = {}
        sec += 1
        for num, info in marbles.items():
            x, y, w, d = info
            nx, ny = x + dxs[d], y + dys[d]
            if (nx, ny) not in new_pos:
                new_marbles[num] = (nx, ny, w, d)
                new_pos[(nx, ny)] = (w, num)
            else:
                last_crash = sec
                prev_w, prev_num = new_pos[(nx, ny)]
                if prev_w < w:
                    new_marbles[num] = (nx, ny, w, d)
                    new_pos[(nx, ny)] = (w, num)
                    del new_marbles[prev_num]
                elif prev_w == w:
                    if prev_num < num:
                        new_marbles[num] = (nx, ny, w, d)
                        new_pos[(nx, ny)] = (w, num)
                        del new_marbles[prev_num]
                    else:
                        new_marbles[prev_num] = (nx, ny, prev_w, d)
                else:
                    new_marbles[prev_num] = (nx, ny, prev_w, d)
        marbles = copy.deepcopy(new_marbles)
        if isEnd(marbles):
            break
    print(last_crash)