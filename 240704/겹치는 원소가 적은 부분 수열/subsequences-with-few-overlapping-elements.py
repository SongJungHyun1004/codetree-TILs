from collections import defaultdict

# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

# map을 이용하여 같은 원소가 몇개 들어있는지 확인합니다.
count_array = defaultdict(lambda: 0)

# 조건을 만족하는 가장 긴 구간의 길이를 구합니다.
ans = 0

# 구간을 잡아봅니다.
j = 0
for i in range(1, n + 1):
    # 구간에 k개 초과하여 겹치는 원소가 없다면 계속 진행합니다.
    while j + 1 <= n and count_array[arr[j + 1]] < k:
        count_array[arr[j + 1]] = count_array[arr[j + 1]] + 1
        j += 1

    # 현재 구간 [i, j]는 
    # i를 시작점으로 하는
    # 가장 긴 구간이므로
    # 구간 크기 중 최댓값을 갱신합니다.
    ans = max(ans, j - i + 1)

    # 다음 구간으로 넘어가기 전에
    # arr[i]에 해당하는 값은 구간에서 제외시킵니다.
    count_array[arr[i]] -= 1

# 정답을 출력합니다.
print(ans)