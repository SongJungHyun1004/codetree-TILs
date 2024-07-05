# 변수 선언 및 입력:
n = int(input())
words = input().split()


class TrieNode:
    def __init__(self):
        # 각 노드에는 'a'부터 'z'까지의 문자에 대응되는 26개의 노드 정보가 관리됩니다.
        self.children = [None] * 26
        # 해당 노드를 기점으로 완성되는 단어 번호를 관리합니다.
        self.end_word_idx = -1
        # 해당 노드가 몇 번째 문자(depth)에 해당하는 노드인지를 관리합니다.
        self.depth = 0
        # 그 다음 문자를 시작으로 하는 단어 중 맨끝 문자까지 봤을 때 정확히 팰린드롬이 되는 경우 중
        # 가장 긴 길이를 관리합니다. 불가능할 시 -1을 넣어줍니다.
        self.max_palin_length = -1


def is_palindrome(s, start_idx):
    # 문자열 s의 start_idx부터 끝까지로 이루어진 부분문자열이 팰린드롬인지를 확인합니다.
    return s[start_idx:] == s[start_idx:][::-1]


def insert_word(root, word, word_idx):
    # 단어 word를 Trie에 넣어줍니다.
    node = root
    for i, char in enumerate(word):
        index = ord(char) - ord('a')
        # 해당하는 노드가 아직 없다면 새로운 노드를 만들어줍니다.
        if node.children[index] is None:
            node.children[index] = TrieNode()

        node = node.children[index]
        # depth를 기록해줍니다.
        node.depth = i + 1
        # 그 다음 문자를 시작으로 하는 단어 중 맨끝 문자까지 봤을 때 정확히 팰린드롬이 된다면
        # 해당 길이 중 최댓값을 갱신해줍니다.
        if i < len(word) - 1 and is_palindrome(word, i + 1):
            node.max_palin_length = max(node.max_palin_length, len(word) - i - 1)

    # 마지막 지점에는 해당 단어의 번호를 적어줍니다.
    node.end_word_idx = word_idx


def search_word(root, word, word_idx):
    global ans

    # 단어 word를 탐색하며 해당 단어로 끝까지 진행했을 때
    # 남은 부분도 팰린드롬으로서 채워줄 수 있는 부분에 대해 확인해봅니다.
    reversed_word = word[::-1]
    node = root
    for i, char in enumerate(reversed_word):
        index = ord(char) - ord('a')
        if node.children[index] is None:
            return

        node = node.children[index]

        # 단어의 끝인 지점이라면 남은 부분의 팰린드롬 여부를 판단하여
        # 그러한 경우 답을 갱신합니다.
        if node.end_word_idx != -1 and node.end_word_idx != word_idx and is_palindrome(reversed_word, i + 1):
            ans = max(ans, len(word) + node.depth)

    # 최종적으로 도착한 위치에서 다른 단어와 연결될 수 있는 가능성이 있다면 답을 갱신합니다.
    if node.max_palin_length != -1:
        ans = max(ans, len(word) * 2 + node.max_palin_length)
    

root = TrieNode()
for idx, word in enumerate(words):
    insert_word(root, word, idx)

ans = 0
for idx, word in enumerate(words):
    search_word(root, word, idx)

print(ans)