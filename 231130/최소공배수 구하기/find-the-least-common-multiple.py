n, m = map(int, input().split())
ni, mi = 1, 1
tn, tm = n*ni, m*mi
while tn != tm:
    if tn < tm:
        ni += 1
        tn = n*ni
    else:
        mi += 1
        tm = m*mi

print(tn)