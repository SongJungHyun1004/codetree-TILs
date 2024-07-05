import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())
words = list(input().split())

ans = 0


# Trie에 사용되는 노드를 정의합니다.
class TrieNode():
    # 생성자입니다.
    def __init__(self):
        # 해당 노드를 거쳐가는 단어가 몇 개 있는지 관리합니다.
        self.num = 0

        # 각 노드에는 'a'부터 'z'까지의 문자에 대응되는 26개의 노드 정보가 관리됩니다.
        # 각 문자에 대응되는 노드 정보는 처음에 None이 됩니다.
        self.children = [None for _ in range(26)]


# 루트 노드에 해당하는 TrieNode를 처음 만들어줍니다.
root = TrieNode()


# 단어 s를 Trie에 넣어줍니다.
def insert_word(s):
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
        t.num += 1 # 단어를 만드는 중이므로 지나가는 노드마다 1씩 더해줍니다.


# Trie를 탐색하며
# 문자열의 길이 * 이 문자열을 접두사로 하는 사전 내에 있는 서로 다른 단어의 수
# 중 최댓값을 계산합니다.
def search_trie(node, depth):
    global ans

    # 각 노드의 위치에서 정답을 갱신해줍니다.
    ans = max(ans, depth * (node.num))

    # 모든 노드를 탐색해줍니다.
    for index in range(26):
        # 만약 노드가 연결되어 있다면
        # 해당 노드를 출력해준 뒤 탐색해줍니다.
        if node.children[index] is not None:
            search_trie(node.children[index], depth + 1)

   
# Trie에 단어들을 넣어줍니다.
for word in words:
    insert_word(word)

# Trie를 탐색하며
# 문자열의 길이 * 이 문자열을 접두사로 하는 사전 내에 있는 서로 다른 단어의 수
# 중 최댓값을 계산합니다.
search_trie(root, 0)

print(ans)