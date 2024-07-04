n, k = tuple(map(int, input().split()))
arr = [
    int(input())
    for _ in range(n)
]
R = [0] * n

# R 배열을 채워줍니다.
# Ri = i + 1번째부터 N번째 까지 있는 숫자들 중
# arr[i]와 숫자가 같은 폭탄 중
# 가장 가까이에 있는 폭탄의 index
# 만약 그러한 폭탄이 없다면 -1을 넣어줍니다.

# 이때 각 숫자별(key)로 가장 가까이에 있는 위치(value)를
# 바로 찾아내기 위해 hashmap을 사용합니다.
latest_index = dict()
for i in range(n - 1, -1, -1):
    # latest_index에 arr[i]가 존재하지 않는다면
    # 최초로 나온 숫자이므로 -1을 넣어줍니다.
    if arr[i] not in latest_index:
        R[i] = -1
    # 이미 arr[i]가 나온적이 있다면
    # 최근에 나온 index를 latest_index에서 찾아 넣어줍니다.
    else:
        R[i] = latest_index[arr[i]]

    # arr[i]가 가장 최근에 등장한 index의 위치를
    # i로 갱신해줍니다.
    latest_index[arr[i]] = i

# 답을 구해줍니다.
# 현재 위치 i에 대해
# 오른쪽에 있으면서 가장 가까이에 있는 동일한 숫자 위치를 구해
# K 이내에 있는지를 확인하고
# 그런 경우에 한하여 번호 중 최댓값을 갱신합니다.
ans = -1
for i in range(n):
    # R[i]가 -1이 아니면서
    # R[i]와 i와의 차이가 K 이하 라면
    # arr[i]는 답의 후보가 됩니다.
    if R[i] != -1 and R[i] - i <= k:
        ans = max(ans, arr[i])

print(ans)