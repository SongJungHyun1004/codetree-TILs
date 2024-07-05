MAX_N = 200001

# 변수 선언 및 입력:
n, q = tuple(map(int, input().split()))
temp = input()

# A : i번지를 중심으로 하는 홀수 길이의 팰린드롬 중 
#     가장 긴 팰린드롬의 반지름의 길이
# 즉, [i - A[i], i + A[i]]가 i를 중심으로 하는 최장 팰린드롬이 됩니다.
A = [0] * MAX_N

# Manacher's algorithm을 적용하기 위해
# 주어진 문자열 내 문자 사이사이에 #을 넣어줍니다.    
input_str = "#" + "#".join(temp) + "#"

# Manacher's algorithm을 진행해봅니다.
n = len(input_str)
r, p = -1, -1
# r : j < i를 만족하는 j들 중 max(j + A[j]) 값을 기록합니다.
# p : max(j + A[j]) 가 되는 j의 값을 기록합니다.
for i in range(n):
    # 만약 r값이 i보다 작다면
    # 줄일 수 있는 부분이 없으므로
    # A[i] = 0으로 시작합니다.
    if r < i:
        A[i] = 0
    # r값이 i보다 같거나 크다면
    # i를 p로부터 대칭시켰을 때의 위치인 ii에 대해
    # 이미 계산된 A[ii]값을 이용하여
    # i를 중심으로 뻗어나갈 수 있는 적절한 초기값을 
    # O(1)에 정해줄 수 있습니다.
    else:
        ii = 2 * p - i
        A[i] = min(r - i, A[ii])

    # i를 중심으로 최대로 뻗어나갑니다.
    while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and \
          input_str[i - A[i] - 1] == input_str[i + A[i] + 1]:
        A[i] += 1 

    # i + A[i] 중 최대가 선택되도록
    # r, p값을 갱신해줍니다.
    if i + A[i] > r:
        r, p = i + A[i], i

# q개의 질의에 대한 답을 처리합니다.
for _ in range(q):
    a, b = tuple(map(int, input().split()))
    
    a -= 1
    b -= 1

    # 처음 주어진 문자열에서 a번 인덱스와 b번 인덱스는 각각
    # 새로 만들어진 문자열에서 2 * a - 1와 2 * b - 1입니다.
    a = 2 * a + 1
    b = 2 * b + 1

    # (a + b) / 2의 위치에서 최장 팰린드롬의 길이를 확인합니다.
    # 만약 a ~ b까지의 문자열보다 최장 팰린드롬의 길이가 길다면
    # 해당 문자열은 팰린드롬이 맞습니다.
    mid = (a + b) // 2
    max_len = 2 * A[mid] + 1
    if max_len >= b - a + 1:
        print("Yes")
    else:
        print("No")