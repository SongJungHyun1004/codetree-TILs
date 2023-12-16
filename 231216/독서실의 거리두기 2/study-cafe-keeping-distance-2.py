n = int(input())
study_room = input()

def find_two_minmaxdist(study_room, flag):
    s = study_room.find('1')
    max_dist = 0
    min_dist = len(study_room)
    for i in range(s+1, len(study_room)):
        if study_room[i] == '1':
            dist = i - s
            if max_dist < dist:
                max_dist = dist
                mx_x, mx_y = s, i
            if min_dist > dist:
                min_dist = dist
                mn_x, mn_y = s, i
            s = i
    if flag == 'max':
        return mx_x, mx_y, None
    else:
        return mn_x, mn_y, min_dist

study_room = list(study_room)
x, y, e = find_two_minmaxdist(''.join(study_room), 'max')
sr1 = study_room[:]
sr2 = study_room[:]
sr3 = study_room[:]
sr1[x+(y-x)//2] = '1'
sr1 = ''.join(sr1)
if sr2[-1] != '1':
    sr2[-1] = '1'
else:
    sr2 = ['1','1']
sr2 = ''.join(sr2)
if sr3[0] != '1':
    sr3[0] = '1'
else:
    sr3 = ['1','1']
sr3 = ''.join(sr3)
x1, y1, d1 = find_two_minmaxdist(sr1, 'min')
x2, y2, d2 = find_two_minmaxdist(sr2, 'min')
x3, y3, d3 = find_two_minmaxdist(sr3, 'min')
if d1 == max(d1, d2, d3):
    print(y1-x1)
    exit(0)
elif d2 == max(d1, d2, d3):
    print(y2-x2)
    exit(0)
elif d3 == max(d1, d2, d3):
    print(y3-x3)
    exit(0)