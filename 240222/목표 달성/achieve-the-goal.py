n, a, b, c, d = map(int, input().split())
# 효율 좋은 애 부터
if a/b < c/d:
    a, c = c, a
    b, d = d, b

energy = 0
energy += (n//a)*b
n %= a
energy += (n//c)*d
n %= c

print(energy)