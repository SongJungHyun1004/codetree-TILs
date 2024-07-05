import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n, _ = tuple(map(int, input().split()))
words = list(input().split())


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


# 단어 s를 탐색하며
# 해당 단어를 접두사로 하는 서로 다른 단어의 수를 계속 출력합니다.
def search_word(s):
    # root에서 시작합니다.
    t = root
    for char in s:
        # 해당하는 노드를 계속 따라갑니다.
        if t is not None:
            index = ord(char) - ord('a')
            t = t.children[index]
        
        # 한 글자 한 글자 입력 될때마다
        # 해당 글자를 시작으로 하는 (거쳐가는) 단어의 수를 출력합니다.
        if t is not None:
            print(t.num, end=" ")
        # 더 이상 그러한 노드가 없다면 답은 0이 됩니다.
        else:
            print(0, end=" ")

   
# Trie에 단어들을 넣어줍니다.
for word in words:
    insert_word(word)

# 단어를 검색합니다.
S = input()
search_word(S)