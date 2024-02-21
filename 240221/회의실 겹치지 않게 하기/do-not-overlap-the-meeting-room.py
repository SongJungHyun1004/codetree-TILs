n = int(input())
requests = []
for _ in range(n):
    s, e = map(int, input().split())
    requests.append((s, e))
requests = sorted(requests, key=lambda x: x[1])
checked = 0
last_e = -1
for s, e in requests:
    if last_e <= s:
        checked += 1
        last_e = e
print(n-checked)