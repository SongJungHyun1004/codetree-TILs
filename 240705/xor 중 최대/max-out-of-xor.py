# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))


# Trie에 사용되는 노드를 정의합니다.
class TrieNode():
    # 생성자입니다.
    def __init__(self):
        # 각 노드에는 '0'부터 '1'까지의 문자에 대응되는 2개의 노드 정보가 관리됩니다.
        self.children = [None for _ in range(2)]


# 루트 노드에 해당하는 TrieNode를 처음 만들어줍니다.
root = TrieNode()

# p2[i] = 2의 i제곱. 값들을 계산하기에 앞서 미리 전처리합니다.
p2 = [0] * 32
p2[0] = 1
for i in range(1, 31):
    p2[i] = p2[i - 1] * 2


# 숫자를 31자리 2진수 문자열로 변환해줍니다.
def convert_to_string(x):
    ret = ""
    for i in range(30, -1, -1):
        if x >= p2[i]:
            x -= p2[i]
            ret += "1"
        else:
            ret += "0"

    return ret


# 단어 s를 Trie에 넣어줍니다.
def insert_word(s):
    # root에서 시작합니다.
    t = root

    for i in range(len(s)):
        # 문자 순서대로 따라가면 됩니다.
        # '0'부터 '1'까지 사용되므로
        # 각각을 0부터 1까지의 index로 매핑시켜줍니다.
        index = ord(s[i]) - ord('0')
        # 해당하는 노드가 아직 없다면 새로운 노드를 만들어줍니다.
        if t.children[index] is None:
            t.children[index] = TrieNode()
        
        # index에 해당하는 노드로 옮겨갑니다.
        t = t.children[index]


# Trie에서 각 단어들을 xor한 최댓값을 탐색합니다.
# 각 자릿수에서 xor했을 때 1이 될 수 있도록 탐색하며 내려갑니다.
def search_word(s):
    ret = ""
    # root에서 시작합니다.
    t = root

    for i in range(len(s)):
        index = ord(s[i]) - ord('0')

        # 만약 1 - index가 있다면, 그쪽으로 따라갑니다.
        if t.children[1 - index] is not None:
            t = t.children[1 - index]
            ret += "1"
        # 없다면 반대쪽으로 따라갑니다.
        else:
            t = t.children[index]
            ret += "0"

    # ret 문자열을 십진수로 표현해서 출력합니다.
    return_value = 0
    for i in range(len(ret)):
        return_value *= 2
        return_value += ord(ret[i]) - ord('0')

    return return_value


# Trie에 단어들을 넣어줍니다.
for i in range(n):
    insert_word(convert_to_string(arr[i]))


# Trie에서 각 단어들을 xor한 최댓값을 탐색합니다.
# 각 자릿수에서 xor했을 때 1이 될 수 있도록 탐색하며 내려갑니다.
ans = 0
for i in range(n):
    num = search_word(convert_to_string(arr[i]))

    ans = max(ans, num)


# 답을 출력합니다.
print(ans)