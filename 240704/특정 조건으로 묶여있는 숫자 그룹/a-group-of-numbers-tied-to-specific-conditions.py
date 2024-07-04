# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = [0] + [
    int(input())
    for _ in range(n)
]
L, R = [0] * (n + 1), [0] * (n + 1)

# 숫자들을 정렬해줍니다.
arr.sort()

# L 배열을 two pointer 방식을 통해 채워줍니다.
# L[i] = 1번부터 i번까지의 숫자들 중
#        정확히 조건을 만족하는 하나의 그룹을 만든다고 했을 때
#        포함할 수 있는 숫자의 개수 중 최댓값
max_num = 0
i = 1
for j in range(1, n + 1):
    # 구간 내 차이가 K를 넘는다면 계속 진행합니다.
    while i + 1 <= j and arr[j] - arr[i] > k:
        i += 1
    
    # 현재 구간 [i, j]는 
    # j를 끝점으로 하는
    # 가장 긴 구간이므로
    # 구간 크기 중 최댓값을 갱신합니다.
    max_num = max(max_num, j - i + 1)

    # 해당 최댓값을 계속 L배열에 넣어줍니다.
    L[j] = max_num

# R 배열을 two pointer 방식을 통해 채워줍니다.
# R[i] = i번부터 n번까지의 숫자들 중
#        정확히 조건을 만족하는 하나의 그룹을 만든다고 했을 때
#        포함할 수 있는 숫자의 개수 중 최댓값
max_num = 0
j = n
for i in range(n, 0, -1):
    # 구간 내 차이가 K를 넘는다면 계속 진행합니다.
    while j - 1 >= i and arr[j] - arr[i] > k:
        j -= 1
    
    # 현재 구간 [i, j]는 
    # i를 시작점으로 하는
    # 가장 긴 구간이므로
    # 구간 크기 중 최댓값을 갱신합니다.
    max_num = max(max_num, j - i + 1)

    # 해당 최댓값을 계속 R배열에 넣어줍니다.
    R[i] = max_num

# i번째 위치를 경계로 
# [1 ~ i], [i + 1 ~ n] 이렇게 2개의 그룹을 만들 영역을 나눴다고 했을 때
# 가능한 최대 원소의 수를 구합니다.
# 단, 여기서 초기값을 L[n]으로 하여
# 단 하나의 그룹만 이용했을 때를 고려해줍니다.
ans = L[n]
for i in range(1, n):
    ans = max(ans, L[i] + R[i + 1])

print(ans)