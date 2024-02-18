n, m = map(int, input().split())
jewelry = []
for _ in range(n):
    w, v = map(int, input().split())
    jewelry.append((w, v))
jewelry = sorted(jewelry, key=lambda x: x[1]/x[0], reverse=True)
value = 0
for w, v in jewelry:
    if m >= w:
        value += v
        m -= w
    else:
        value += v * m/w
        break
print(f'{value:.3f}')