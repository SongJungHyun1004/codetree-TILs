# 변수 선언 및 입력:
text, q = tuple(input().split())
q = int(q)

for _ in range(q):
    pattern = input()

    n = len(text)
    m = len(pattern)

    # failure function입니다.
    # f[i] : pattern에서 
    #        [1, i]로 이루어진 문자열 중
    #        접두사와 접미사가 일치하는 최장 길이 (단, 자기자신은 제외)
    f = [0] * (m + 1)

    # 구현의 편의를 위해 맨 앞에 #을 붙여
    # 문자열을 1번지부터 사용합니다.
    text = "#" + text
    pattern = "#" + pattern

    # failure function값을 먼저 계산합니다.
    f[0] = -1 # f[0]은 구현의 편의를 위해 -1로 설정합니다.
    for i in range(1, m + 1):
        # 시작은 최적의 답에 해당하는 f[i - 1]에서 합니다.
        # 그 전 위치까지 최적의 (접두사, 접미사) 매칭 결과 바로 뒤에
        # 추가되는 것이 가능하다면 최적의 답이 되기 때문입니다.
        j = f[i - 1]
        # [1, i - 1]까지는
        # 정확히 길이 j만큼 접두사와 접미사가 일치한다고 했을 때
        # 그 다음 문자인 pattern[j + 1]과 pattern[i]가 일치하는지를 확인합니다.
        # 일치하지 않는다면 그 다음 후보로 j값을 옮겨줍니다.
        while j >= 0 and pattern[j + 1] != pattern[i]:
            j = f[j]

        # [1, i - 1]까지 일치하며 동시에 그 다음 문자까지 일치하는 최대 j가 구해져있으므로
        # 이제 그 값에 1을 더한 결과가 f[i]가 됩니다.
        # 매칭에 실패했더라도 f[0]에는 -1이 들어있기에
        # f[i] = 0이 됩니다.
        f[i] = j + 1

    # 한 문자씩 비교하며 패턴 문자열과 일치하게 되는 순간을 구합니다.
    ans = 0
    j = 0
    for i in range(1, n + 1):
        # text의 [i - j, i - 1]와 pattern의 [1, j]가 일치한다는 가정 하여
        # 그 다음 문자인 pattern[j + 1]와 text[i]를 비교합니다.
        # 일치하지 않는다면 f를 이용하여 그 다음 후보로 j값을 빠르게 옮겨줍니다.
        while j >= 0 and pattern[j + 1] != text[i]:
            j = f[j]
        
        # 일치하는 곳에서 빠져나온 것이기에
        # 이제 j를 1만큼 증가시킵니다.
        # 매칭에 실패했더라도 j = -1에서 끝났을 것이기에
        # 그 다음 j는 0이 됩니다.
        j += 1
        
        # j가 m이 되면 전부 일치했다는 뜻이므로 
        # 답을 갱신해주고 다시 그 다음 후보로 넘어갑니다.
        if j == m:
            ans += 1
            j = f[j]
    
    print(ans)