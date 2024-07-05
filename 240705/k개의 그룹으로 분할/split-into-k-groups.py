# 변수 선언
n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

# dp[i] : 
# 1부터 n까지 방문한 숫자들의 여부를 (0, 1)로 나타냈을 때
# x1, x2, ..., xk라 했을 때 
# 2^x1 + 2^x2 + ... + 2^xk 값이 i일 때 (bitmask된 정수값이 i)
# 그렇게 구간을 두는 것이 가능한지 여부 (구현의 편의를 위해 총합을 저장합니다)
dp = [-1] * (1 << n)
dp[0] = 0

# 각 그룹의 숫자의 합이 몇이어야 하는지 판단합니다.
s = sum(a)

# 총합이 k의 배수가 아니라면 k개의 그룹으로 나누는 것이 불가능합니다.
if s % k:
    print("No")
else:
    part = s // k

    # 뿌려주는 방식의 dp를 진행합니다.
    # dp[i]가 계산이 되어 있다는 가정하에서
    # 그 다음 상태값을 갱신합니다.
    for i in range(1 << n):
        if dp[i] == -1:
            continue
        # 그 다음으로 그룹에 j번 숫자를 넣는 경우를 계산해 줍니다.
        for j in range(1, n + 1):
            # j번 지점을 이미 방문한 적이 있다면
            # 중복 방문은 조건상 불가하므로 패스합니다.
            if (i >> (j - 1)) & 1:
                continue
            
            num = dp[i] % part
            # 만약 합을 구했을 때 part를 넘는다면 패스합니다.
            if num + a[j] > part:
                continue
            
            dp[i | (1 << (j - 1))] = dp[i] + a[j]

    # 만약 k개의 그룹으로 만들 수 있다면 dp[(1 << n) - 1]에 s가 들어갑니다.
    print("Yes" if dp[(1 << n) - 1] == s else "No")