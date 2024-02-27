y, m, d = map(int, input().split())
day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leapyear(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True
    return False

def which_season(m):
    if 3 <= m <= 5:
        return 'Spring'
    elif 6 <= m <= 8:
        return 'Summer'
    elif 9 <= m <= 11:
        return 'Fall'
    else:
        return 'Winter'

if is_leapyear(y):
    day[2] += 1
if day[m] < d:
    print(-1)
else:
    print(which_season(m))