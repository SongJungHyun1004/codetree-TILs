n = int(input())
reservation = []
for _ in range(n):
    s, e = map(int, input().split())
    reservation.append((s, +1))
    reservation.append((e, -1))
reservation = sorted(reservation)
cnt = 0
mx = 0
for _, v in reservation:
    cnt += v
    mx = max(mx, cnt)
print(mx)