# 변수 선언 및 입력:
n, pattern = tuple(input().split())
n = int(n)
l = len(pattern)

edges = [[] for _ in range(n + 1)]
path = [0] * (n + 1)

for _ in range(n - 1):
    x, y, c = tuple(input().split())
    x, y = int(x), int(y)
    edges[x].append((y, c))

# 2개의 polynomial rolling 해싱을 위한 p, m 값을 정의합니다.
p = [31, 37]
m = [int(1e9) + 7, int(1e9) + 9]

# p^i, 값을 m으로 나눈 나머지를 관리합니다.
p_pow = [
    [0] * (n + 1)
    for _ in range(2)
]

# 처음 주어진 패턴에 대한 해싱값을 관리합니다.
p_h = [0, 0]

ans = 0


# 소문자 알파벳을 수로 변경합니다.
def to_int(c):
    return ord(c) - ord('a') + 1


def dfs(x, cnt, t_h1, t_h2):
    global ans

    t_h = [t_h1, t_h2]

    # 해싱값을 계산해줍니다.
    if cnt == l:
        # text에서 구간 [0, l - 1]에 해당하는 해싱값을 계산합니다.
        for k in range(2):
            for i in range(l):
                t_h[k] = (t_h[k] + to_int(path[i]) * p_pow[k][l - 1 - i]) % m[k]
    elif cnt > l:
        for k in range(2):
            # 이전 [cnt - l - 1, cnt - 2]에 해당하는 해싱값은 t_h에 있습니다.
            # 이전 값(t_h)은 (T[cnt - l - 1] * p^(l - 1) + T[cnt - l] * p^(l - 2) + ... + T[cnt - 2] * 1) % m입니다.
            # 이제 t_h * p - T[cnt - l - 1] * p^l + T[cnt - 1]를 계산하면
            # 새로 계산을 원하는 해싱값인 (T[cnt - l] * p^(l - 1) + T[cnt - l + 1] * p^(l - 2) + ... + T[cnt - 1] * 1) % m이 됩니다.
            t_h[k] = (t_h[k] * p[k] - to_int(path[cnt - l - 1]) * p_pow[k][l] + to_int(path[cnt - 1])) % m[k]
            # t_h값을 양수로 변환해줍니다.
            if t_h[k] < 0:
                t_h[k] += m[k]

    # 일치하면 답을 갱신해줍니다.
    if t_h[0] == p_h[0] and t_h[1] == p_h[1]:
        ans += 1

    for y, c in edges[x]:
        path[cnt] = c
        dfs(y, cnt + 1, t_h[0], t_h[1])


# p_pow 값을 계산합니다.
for k in range(2):
    # p_pow[i] = p^i % m
    p_pow[k][0] = 1
    for i in range(1, n + 1):
        p_pow[k][i] = (p_pow[k][i - 1] * p[k]) % m[k]

# pattern에 대한 해싱값인 p_h값을 계산합니다.
# p_h = (P[0] * p^(l - 1) + P[1] * p^(l - 2) + ... + P[l - 1] * 1) % m
# 소문자 알파벳은 a부터 z까지 순서대로 1부터 26까지의 수와 대응됩니다.
for k in range(2):
    for i in range(l):
        p_h[k] = (p_h[k] + to_int(pattern[i]) * p_pow[k][l - 1 - i]) % m[k]

dfs(1, 0, 0, 0)

print(ans)