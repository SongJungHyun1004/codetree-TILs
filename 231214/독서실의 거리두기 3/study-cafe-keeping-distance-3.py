n = int(input())
study_room = input()

def find_two_minmaxdist(study_room, flag):
    s = 0
    max_dist = 0
    min_dist = len(study_room)
    for i in range(1, len(study_room)):
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
        return mx_x, mx_y
    else:
        return mn_x, mn_y

x, y = find_two_minmaxdist(study_room, 'max')
study_room = list(study_room)
study_room[x+(y-x)//2] = '1'
study_room = ''.join(study_room)
x, y = find_two_minmaxdist(study_room, 'min')
print(y-x)