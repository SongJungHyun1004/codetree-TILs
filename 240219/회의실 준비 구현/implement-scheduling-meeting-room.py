n = int(input())
reservation = []
for _ in range(n):
    s, e = map(int, input().split())
    reservation.append((s, e))
reservation = sorted(reservation, key=lambda x:x[1])
progress = 0
last_e = - 1
for s, e in reservation:
    if last_e <= s:
        progress += 1
        last_e = e
print(progress)