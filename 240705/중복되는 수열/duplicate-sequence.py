# 변수 선언 및 입력:
n = int(input())
words = [
    input()
    for _ in range(n)
]


# Trie에 사용되는 노드를 정의합니다.
class TrieNode():
    # 생성자입니다.
    def __init__(self):
        # 해당 노드를 기점으로 하나의 단어가 완성되는지를 판단합니다.
        # 단어 완성에 대한 초기값은 False입니다.
        self.is_end = False

        # 각 노드에는 '0'부터 '9'까지의 문자에 대응되는 10개의 노드 정보가 관리됩니다.
        # 각 문자에 대응되는 노드 정보는 처음에 None이 됩니다.
        self.children = [None for _ in range(10)]


# 루트 노드에 해당하는 TrieNode를 처음 만들어줍니다.
root = TrieNode()


# 단어 s를 Trie에 넣어줍니다.
def insert_word(s):
    # root에서 시작합니다.
    t = root
    for char in s:
        # 문자 순서대로 따라가면 됩니다.
        # '0'부터 '9'까지 사용되므로
        # 각각을 0부터 9까지의 index로 매핑시켜줍니다.
        index = ord(char) - ord('0')
        # 해당하는 노드가 아직 없다면 새로운 노드를 만들어줍니다.
        if t.children[index] is None:
            t.children[index] = TrieNode()
        
        # index에 해당하는 노드로 옮겨갑니다.
        t = t.children[index]
    # 최종 위치에 단어의 끝임을 표시해줍니다.
    t.is_end = True


# 단어 s를 탐색하며
# 도중에 끝이라고 표시된 단어가 있는지 판단합니다.
# 만약 그렇다면 접두사에 해당하는 단어가 존재한다는 뜻입니다.
def search_word(s):
    # root에서 시작합니다.
    t = root
    for char in s:
        # 만약 도중에 끝이라고 표시된 단어가 있다면 True를 반환합니다.
        if t.is_end:
            return True
        
        # 해당하는 노드를 계속 따라갑니다.
        index = ord(char) - ord('0')
        t = t.children[index]

    # 끝까지 갔음에도 존재하지 않는다면
    # 그러한 경우가 없다는 뜻입니다.
    return False

   
# Trie에 단어들을 넣어줍니다.
for word in words:
    insert_word(word)

# Trie에서 각 단어들을 탐색하는 도중
# 끝이라고 표시된 단어가 있는지 확인합니다.
# 만약 그렇다면 접두사에 해당하는 단어가 존재한다는 뜻입니다.
exists = False
for word in words:
    if search_word(word):
        exists = True

# 답을 출력합니다.
print(0 if exists else 1)