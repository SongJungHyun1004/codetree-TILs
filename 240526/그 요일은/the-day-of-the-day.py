moths = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
m1, d1, m2, d2 = map(int, input().split())
A = input()

days = 0
for m in range(m1, m2):
    days += moths[m]
days += d2-d1+1

cnt = days//7
if days%7 <= weeks.index(A)+1:
    cnt += 1
print(cnt)