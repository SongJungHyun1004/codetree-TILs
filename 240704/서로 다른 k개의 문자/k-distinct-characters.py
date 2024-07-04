# 변수 선언 및 입력:
word, k = input().split()
k = int(k)
word = "#" + word
n = len(word) - 1
count_array = dict()


# j가 추가적으로 더 앞으로 움직여도 되는지 판단합니다.
def can_move(j):
    # 범위를 벗어난다면 움직일 수 없습니다.
    if j + 1 > n:
        return False

    # 이미 서로 다른 문자의 개수가 k개인데
    # 또 새로운 문자를 추가하는 것이라면
    # 더 움직일 수 없습니다.
    if distinct_number == k and count_array.get(word[j + 1], 0) == 0:
        return False
    
    # 이외에는 움직여도 됩니다.
    return True


# 가능한 구간 중 최대 크기를 구합니다.
ans = 0

# 구간을 잡아봅니다.
distinct_number = 0 # 서로 다른 문자의 수를 저장해줍니다.
j = 0
for i in range(1, n + 1):
    # 서로 다른 문자의 수가 k개가 넘기 전까지 계속 진행합니다.
    while can_move(j):
        count_array[word[j + 1]] = count_array.get(word[j + 1], 0) + 1
        # 새로운 문자가 추가된 것이라면, 서로 다른 문자의 수를 늘려줍니다.
        if count_array[word[j + 1]] == 1:
            distinct_number += 1
        j += 1
    
    # 현재 구간 [i, j]는 
    # i를 시작점으로 하는
    # 가장 긴 구간이므로
    # 구간 크기 중 최댓값을 갱신합니다.
    ans = max(ans, j - i + 1)

    # 다음 구간으로 넘어가기 전에
    # word[i]에 해당하는 값은 count_array에서 지워줍니다.
    count_array[word[i]] -= 1

    # 해당 문자가 사라졌다면, 서로 다른 문자의 수를 하나 줄여줍니다.
    if count_array[word[i]] == 0:
        distinct_number -= 1

print(ans)