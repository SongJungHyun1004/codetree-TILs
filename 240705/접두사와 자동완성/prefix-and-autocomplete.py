import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())
words = list(input().split())


# Trie에 사용되는 노드를 정의합니다.
class TrieNode():
    # 생성자입니다.
    def __init__(self):
        # 해당 노드에서 몇개의 자식 경로가 있는지 판단합니다.
        self.child = 0

        # 해당 노드에서 끝나는 단어가 있는지 판단합니다.
        self.is_end = False

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
            t.child += 1 # 새로운 경로가 추가됩니다.
            t.children[index] = TrieNode()
        
        # index에 해당하는 노드로 옮겨갑니다.
        t = t.children[index]
    
    # 해당 단어가 t노드에서 끝났기 때문에, 끝났음을 표시해줍니다.
    t.is_end = True


def autocomplete_search(s):
    # root에서 시작합니다.
    t = root
    
    cnt = 0
    for char in s:
        # 해당하는 노드를 계속 따라갑니다.
        index = ord(char) - ord('a')

        # 첫 문자를 입력해야 하는 순간이거나
        # 현재 노드로 끝나는 문자가 있어 더이상 자동완성이 진행되지 않거나
        # 자식 경로가 2개 이상이라
        # 자동으로 완성되지 못할 경우
        # 직접 입력해야 하는 문자이므로 1을 더해줍니다.
        if t == root or t.is_end or t.child > 1:
            cnt += 1

        t = t.children[index]

    return cnt

   
# Trie에 단어들을 넣어줍니다.
for word in words:
    insert_word(word)

for word in words:
    print(autocomplete_search(word), end=" ")