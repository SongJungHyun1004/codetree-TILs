str1 = input()
str2 = input()

str1_len, str2_len = len(str1), len(str2)

# string의 index가 0부터 시작하기 때문에
# 이를 1부터 시작하기 위해서 앞에 #을 추가해줍니다.
str1, str2 = '#' + str1, '#' + str2

dp = [
    [0 for _ in range(str2_len + 1)]
    for _ in range(str1_len + 1)
]

def initialize():
    # 아무 것도 없는 상태와 각 문자열의 편집 거리를 초기화해줍니다.
    dp[0][0] = 0
    
    for i in range(1, str1_len + 1):
        dp[i][0] = i
    
    for j in range(1, str2_len + 1):
        dp[0][j] = j
            
initialize()

for i in range(1, str1_len + 1):
    # 첫 번째 문자열의 i 번째까지 문자열을 고려했고
    # 두 번째 문자열의 j 번째까지 문자열을 고려했을 때
    # 가능한 최소 편집 거리를 구해줍니다.
    for j in range(1, str2_len + 1):
        # Case 1:
        # 첫 번째 문자열의 i번째 문자와,  두 번째 문자열 j번째 문자가 일치하는 경우
        # 해당 문자를 편집하지 않는 것이 항상 더 좋으므로
        # 첫 번째 문자열에서 i-1번째 문자까지 고려하고, 
        # 두 번째 문자열의 j-1번째 문자까지 고려했을 때인 dp[i-1][j-1]을 사용합니다. 
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1]
            
        # Case 2:
        # 각 문자를 바꾸거나, 삽입하거나 삭제하는 경우에 대하여
        # 최소 편집 거리를 구해준 뒤 1을 추가해줍니다.
        else:
            dp[i][j] = min(min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1]) + 1
            
print(dp[str1_len][str2_len])