# 변수 선언 및 입력:
n = int(input())
list_of_words = []

for _ in range(n):
    _, *words = tuple(input().split())
    list_of_words.append(words)


# Trie에 사용되는 노드를 정의합니다.
class TrieNode():
    # 생성자입니다.
    def __init__(self):
        # 어떤 문자열이던 자식이 될 수 있도록 dict를 만들어줍니다. 
        self.children = {}


# 루트 노드에 해당하는 TrieNode를 처음 만들어줍니다.
root = TrieNode()


# 단어 리스트 s를 Trie에 넣어줍니다.
def insert_words(words):
    # root에서 시작합니다.
    t = root
    for string in words:
        # 해당하는 노드가 아직 없다면 새로운 노드를 만들어줍니다.
        if string not in t.children:
            t.children[string] = TrieNode()
        
        # string에 해당하는 노드로 옮겨갑니다.
        t = t.children[string]


# 트라이에 있는 모든 노드를 탐색하여
# 트라이 구조를 출력해줍니다.
def search_trie(node, depth):
    # 모든 노드를 탐색해줍니다.
    for key in sorted(node.children.keys()):
        # 만약 노드가 연결되어 있다면
        # 해당 노드를 출력해준 뒤 탐색해줍니다.
        if node.children[key]:
            print("-" * (2 * depth) + key)
            search_trie(node.children[key], depth + 1)


# Trie에 단어들을 넣어줍니다.
for words in list_of_words:
    insert_words(words)

# 트라이에 있는 모든 노드를 탐색하여
# 트라이 구조를 출력해줍니다.
search_trie(root, 0)