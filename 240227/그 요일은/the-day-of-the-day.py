m1, d1, m2, d2 = map(int, input().split())
weekday = input()
days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
day = 0
for i in range(m1+1, m2):
    day += days[i]
day += days[m1]-d1+1
day += d2
weeks = ['Sun','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
for i in range(7):
    if weeks[i] == weekday:
        r = i
        break
cnt = 0
cnt += day // 7
day %= 7
if r <= day:
    cnt += 1
print(cnt)