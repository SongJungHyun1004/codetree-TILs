# 변수 선언 및 입력:
defaultString, m = input().split()
m = int(m)

words = input().split()

n = len(defaultString)

MOD = 10**9 + 7

# Trie에 사용되는 노드를 정의합니다.
class TrieNode():
    # 생성자입니다.
    def __init__(self):
        # 각 노드에는 'a'부터 'z'까지의 문자에 대응되는 26개의 노드 정보가 관리됩니다.
        # 각 문자에 대응되는 노드 정보는 처음에 None이 됩니다.
        self.children = [None for _ in range(26)]

        # 해당 노드를 기점으로 하나의 단어가 완성되는지를 판단합니다.
        self.is_end = False


# 루트 노드에 해당하는 TrieNode를 처음 만들어줍니다.
root = TrieNode()


dp = [0 for _ in range(n + 1)]


# 단어 s를 Trie에 넣어줍니다.
def InsertWord(s):
    # root에서 시작합니다.
    t = root
    for char in s:
        # 문자 순서대로 따라가면 됩니다.
        # 'a'부터 'z'까지 사용되므로
        # 각각을 0부터 25까지의 index로 매핑시켜줍니다.
        index = ord(char) - ord('a')
        # 해당하는 노드가 아직 없다면 새로운 노드를 만들어줍니다.
        if t.children[index] is None:
            t.children[index] = TrieNode()
        
        # index에 해당하는 노드로 옮겨갑니다.
        t = t.children[index]
    
    # 최종 위치에 단어의 끝임을 표시해줍니다.
    t.is_end = True


# idx번째 dp를 갱신해줍니다.
def updateDP(s, idx):
    # root에서 시작합니다.
    t = root

    for i in range(idx, n):
        # 해당하는 노드를 계속 따라갑니다.
        index = ord(s[i]) - ord('a')

        t = t.children[index]

        # 만족하는 트라이가 없다면 멈춥니다.
        if not t: break

        # 해당 위치에 문자열이 존재한다면
        # dp값을 갱신해줍니다.
        if t.is_end:
            dp[i + 1] += dp[idx]
            dp[i + 1] %= MOD


# Trie에 단어들을 넣어줍니다.
for word in words:
    InsertWord(word)

dp[0] = 1

# 순서대로 한칸씩 이동하면서 dp를 갱신해줍니다.
for i in range(n):
    updateDP(defaultString, i)

print(dp[n])