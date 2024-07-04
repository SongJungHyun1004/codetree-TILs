# 변수 선언 및 입력:
word = "#" + input()
n = len(word) - 1
count_array = dict()

# 가능한 구간 중 최대 크기를 구합니다.
ans = 0

# 구간을 잡아봅니다.
j = 0
for i in range(1, n + 1):
    # 같은 문자가 2개가 되기 전까지 계속 진행합니다.
    while j + 1 <= n and count_array.get(word[j + 1], 0) != 1:
        count_array[word[j + 1]] = count_array.get(word[j + 1], 0) + 1
        j += 1
    
    # 현재 구간 [i, j]는 
    # i를 시작점으로 하는
    # 가장 긴 구간이므로
    # 구간 크기 중 최댓값을 갱신합니다.
    ans = max(ans, j - i + 1)

    # 다음 구간으로 넘어가기 전에
    # word[i]에 해당하는 값은 count_array에서 지워줍니다.
    count_array[word[i]] -= 1

print(ans)