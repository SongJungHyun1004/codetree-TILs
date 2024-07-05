# 변수 선언 및 입력:
n = int(input())
words = []

for _ in range(n):
    _, *chars = tuple(input().split())
    words.append("".join(chars))


# Trie에 사용되는 노드를 정의합니다.
class TrieNode():
    # 생성자입니다.
    def __init__(self):
        # 해당 노드를 기점으로 하나의 단어가 완성되는지를 판단합니다.
        # 단어 완성에 대한 초기값은 False입니다.
        self.is_end = False

        # 각 노드에는 'A'부터 'B'까지의 문자에 대응되는 26개의 노드 정보가 관리됩니다.
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
        # 'A'부터 'Z'까지 사용되므로
        # 각각을 0부터 25까지의 index로 매핑시켜줍니다.
        index = ord(char) - ord('A')
        # 해당하는 노드가 아직 없다면 새로운 노드를 만들어줍니다.
        if t.children[index] is None:
            t.children[index] = TrieNode()
        
        # index에 해당하는 노드로 옮겨갑니다.
        t = t.children[index]
    # 최종 위치에 단어의 끝임을 표시해줍니다.
    t.is_end = True


# 트라이에 있는 모든 노드를 탐색하여
# 트라이 구조를 출력해줍니다.
def print_trie(node, depth):
    # 모든 노드를 탐색해줍니다.
    for index in range(26):
        # 만약 노드가 연결되어 있다면
        # 해당 노드를 출력해준 뒤 탐색해줍니다.
        if node.children[index]:
            print("-" * (2 * depth) + chr(ord('A') + index))
            print_trie(node.children[index], depth + 1)


# Trie에 단어들을 넣어줍니다.
for word in words:
    insert_word(word)

# 트라이에 있는 모든 노드를 탐색하여
# 트라이 구조를 출력해줍니다.
print_trie(root, 0)