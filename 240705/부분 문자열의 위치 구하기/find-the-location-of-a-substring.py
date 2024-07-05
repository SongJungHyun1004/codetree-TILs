# 변수 선언 및 입력:
text = input()
pattern = input()

n = len(text)
l = len(pattern)

# 2개의 polynomial rolling 해싱을 위한 p, m 값을 정의합니다.
p = [31, 37]
m = [int(1e9) + 7, int(1e9) + 9]

# p^i, 값을 m으로 나눈 나머지를 관리합니다.
p_pow = [
    [0] * (n + 1)
    for _ in range(2)
]


# 소문자 알파벳을 수로 변경합니다.
def to_int(c):
    return ord(c) - ord('a') + 1


# p_pow 값을 계산합니다.
# p_pow[i] = p^i % m
for k in range(2):
    # p_pow[i] = p^i % m
    p_pow[k][0] = 1
    for i in range(1, n + 1):
        p_pow[k][i] = (p_pow[k][i - 1] * p[k]) % m[k]

# pattern에 대한 해싱값인 p_h값을 계산합니다.
# p_h = (pattern[0] * p^(l - 1) + pattern[1] * p^(l - 2) + ... + pattern[l - 1] * 1) % m
# 소문자 알파벳은 a부터 z까지 순서대로 1부터 26까지의 수와 대응됩니다.
p_h = [0, 0]
for k in range(2):
    for i in range(l):
        p_h[k] = (p_h[k] + to_int(pattern[i]) * p_pow[k][l - 1 - i]) % m[k]

# text에서 구간 [0, l - 1]에 해당하는 해싱값을 계산합니다.
t_h = [0, 0]
for k in range(2):
    for i in range(l):
        t_h[k] = (t_h[k] + to_int(text[i]) * p_pow[k][l - 1 - i]) % m[k]

# 이미 일치한다면 답은 0이 됩니다.
if p_h[0] == t_h[0] and p_h[1] == t_h[1]:
    print(0)
    quit()

# text에서
# 길이가 l인 부분문자열을 전부 잡아보며
# 해싱값이 일치하는 위치를 찾습니다.
ans = -1
for i in range(1, n - l + 1):
    for k in range(2):
        # 이전 [i - 1, i + l - 2]에 해당하는 해싱값은 t_h에 있습니다.
        # 이전 값(t_h)은 (text[i - 1] * p^(l - 1) + text[i] * p^(l - 2) + ... + text[i + l - 2] * 1) % m입니다.
        # 이제 t_h * p - text[i - 1] * p^l + text[i + l - 1]를 계산하면
        # 새로 계산을 원하는 해싱값인 (text[i] * p^(l - 1) + text[i + 1] * p(l - 2) + ... + text[i + l - 1] * 1) % m이 됩니다.
        t_h[k] = (t_h[k] * p[k] - to_int(text[i - 1]) * p_pow[k][l] + to_int(text[i + l - 1])) % m[k]
        # t_h값을 양수로 변환해줍니다.
        if t_h[k] < 0:
            t_h[k] += m[k]

    # 값이 일치한다면 답이 됩니다.
    if p_h[0] == t_h[0] and p_h[1] == t_h[1]:
        ans = i
        break

print(ans)