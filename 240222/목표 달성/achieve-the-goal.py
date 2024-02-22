n, a, b, c, d = map(int, input().split())
# 효율 좋은 애 부터
if b/a > d/c: # 1만큼 일할 때 에너지가 작은것이 효율이 더 좋다
    a, c = c, a
    b, d = d, b

energy = 0
energy += (n//a)*b
n %= a
energy += (n//c)*d
n %= c
if n:
    energy += min(b, d)
print(energy)