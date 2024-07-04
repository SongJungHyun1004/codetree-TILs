import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))
count_array_in  = [0] * (m + 1) # 구간 내 숫자 정보
count_array_out = [0] * (m + 1) # 구간 외 숫자 정보

distinct_num_in  = 0 # 구간 내 서로 다른 숫자 개수
distinct_num_out = 0 # 구간 외 서로 다른 숫자 개수


# arr[idx] 숫자를 구간에 집어넣게 되었을 때의
# count_array와 distinct_num 값을 갱신해줍니다.
def push(idx):
    global distinct_num_in, distinct_num_out
    num = arr[idx]

    # 구간 내로 새로 들어온 숫자라면 
    # 숫자 종류가 하나 늘어납니다. 
    if count_array_in[num] == 0:
        distinct_num_in += 1
    count_array_in[num] += 1

    # num과 동일한 구간 외 숫자가
    # 이제 존재하지 않는다면, 숫자 종류를 하나 감소시켜줍니다.
    count_array_out[num] -= 1
    if count_array_out[num] == 0:
        distinct_num_out -= 1


# arr[idx] 숫자를 구간에서 빼게 되었을 때의
# count_array와 distinct_num 값을 갱신해줍니다.
def pop(idx):
    global distinct_num_in, distinct_num_out
    num = arr[idx]

    # num과 동일한 구간 내 숫자가 
    # 이제 존재하지 않는다면, 숫자 종류를 하나 감소시켜줍니다.
    count_array_in[num] -= 1
    if count_array_in[num] == 0:
        distinct_num_in -= 1

    # 구간 외 공간으로 새로 들어온 숫자라면 
    # 숫자 종류가 하나 늘어납니다.
    if count_array_out[num] == 0:
        distinct_num_out += 1 
    count_array_out[num] += 1


# 구간 외 숫자 정보에 대한 초기 값을 계산합니다.
for i in range(1, n + 1):
    # 최초로 적히는 순간이라면
    # 숫자 종류가 하나 늘어납니다.
    if count_array_out[arr[i]] == 0:
        distinct_num_out += 1
    
    count_array_out[arr[i]] += 1

# 가능한 구간 중 최소 크기를 구합니다.
ans = INT_MAX

# 구간을 잡아봅니다.
j = 0
for i in range(1, n + 1):
    # 구간 내에 1에서 m까지의 숫자가 전부 포함되지 않는한 계속 진행합니다.
    while j + 1 <= n and distinct_num_in < m:
        push(j + 1)
        j += 1

    # 계속 전진했음에도 결국 1에서 m 숫자를 전부 포함하지 못했다면
    # 탐색을 종료합니다.
    if distinct_num_in < m:
        break
    
    # 현재 구간 [i, j]는 
    # i를 시작점으로 하는
    # 가장 짧은 구간이며
    # 만약 구간 외에도 1에서 m 사이의 숫자가 전부 있는 경우라면
    # 구간 크기 중 최솟값을 갱신합니다.
    if distinct_num_out == m:
        ans = min(ans, j - i + 1)

    # 다음 구간으로 넘어가기 전에
    # arr[i]에 해당하는 값을 구간에서 제외해줍니다.
    pop(i)

# 불가능하다면 -1을 출력합니다.
if ans == INT_MAX:
    ans = -1

print(ans)