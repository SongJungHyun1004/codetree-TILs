MAX_N = 100002
MAX_M = 10

class Node:
    # 사람들을 나타내는 노드입니다.
    def __init__(self, id):
        # 사람의 번호를 나타냅니다.
        self.id = id
        self.prev = None
        self.next = None

def connect(s, e):
    # 두 사람을 연결합니다.
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

# i번 사람을 집에 보냅니다.
def pop(i):
    # i번 사람이 어느 줄에 서있는지 확인합니다.
    l = lineNum[i.id]
    
    # i번 사람이 어느 줄에도 서있지 않다면 아무것도 하지 않습니다.
    if l == 0:
        return
    # i번 사람이 줄의 시작이었다면 줄의 시작을 다음 사람으로 바꿉니다.
    if head[l] == i:
        head[l] = i.next
    # i번 사람이 줄의 끝이었다면 줄의 끝을 이전 사람으로 바꿉니다.
    if tail[l] == i:
        tail[l] = i.prev

    # i번 사람을 줄에서 뺍니다.
    # 원래 i번 사람의 이전 사람과 다음 사람을 연결합니다.
    if i.prev is not None:
        i.prev.next = i.next
    if i.next is not None:
        i.next.prev = i.prev

    # i번 사람이 어느 줄에도 서있지 않다고 표시합니다.
    lineNum[i.id] = 0
    i.next = i.prev = None

def insertFront(a, b):
    # a번 사람을 b번 사람 앞에 서게 합니다.
    lineNumB = lineNum[b.id]

    # b번 사람이 어느 줄에 서있는지 확인합니다.
    if head[lineNumB] == b:
        head[lineNumB] = a

    # b번 사람이 해당 줄의 맨 앞이었다면, a번 사람을 줄의 맨 앞으로 만듭니다.
    pop(a)
    connect(b.prev, a)
    connect(a, b)

    # a번 사람을 해당 줄에서 뺍니다.
    lineNum[a.id] = lineNumB

    # a번 사람을 b번 사람 앞에 서게 합니다.
def popRangeAndInsertPrev(a, b, c):
    # a번 사람부터 b번 사람까지를 c번 사람 앞에 이동합니다.
    lineNumA = lineNum[a.id]
    lineNumC = lineNum[c.id]

    # a, c번 사람이 어느 줄에 서있는지 확인합니다.
    if head[lineNumA] == a:
        head[lineNumA] = b.next
    if tail[lineNumA] == b:
        tail[lineNumA] = a.prev

    # a번 사람이 해당 줄의 맨 앞이었다면, 해당 줄의 맨 앞 사람을 b번 사람의 뒤로 변경합니다.
    connect(a.prev, b.next)
    if head[lineNumC] == c:
        head[lineNumC] = a
    else:
        connect(c.prev, a)

    # b번 사람이 해당 줄의 맨 끝이었다면, 해당 줄의 맨 끝 사람을 a번 사람의 앞으로 변경합니다.
    connect(b, c)
    cur = a

    # a번 사람부터 b번 사람까지를 줄에서 뺍니다.
    while cur != b.next:
        lineNum[cur.id] = lineNumC
        cur = cur.next

    # 이때 a번 사람의 이전 사람과 b번 사람의 다음 사람을 연결합니다.

def printLine(l):
    # 해당 줄을 전부 출력합니다.
    cur = head[l]
    if cur is None:
        print(-1)
    else:
        while cur is not None:
            print(cur.id, end=" ")
            cur = cur.next
        print()
import math
n, m, q = map(int, input().split())
x = n//m
# m 개의 줄을 입력 받습니다.
nodes = {}
head = [None] * (MAX_M + 1)
tail = [None] * (MAX_M + 1)
lineNum = {}
people = ['']+list(input().split())
cnt = 0
for i in range(1, m + 1):
    line = people[1+x*cnt:1+x*cnt+x]
    for j in range(x):
        t = line[j]
        lineNum[t] = i
        nodes[t] = Node(t)
        if j == 0:
            head[i] = tail[i] = nodes[t]
        else:
            connect(tail[i], nodes[t])
            tail[i] = nodes[t]
    cnt += 1

# q 개의 문자대로 시뮬레이션을 진행합니다.
for _ in range(q):
    option = list(input().split())

    if option[0] == '1':
        a, b = option[1], option[2]
        insertFront(nodes[a], nodes[b])
    elif option[0] == '2':
        a = option[1]
        pop(nodes[a])
    elif option[0] == '3':
        a, b, c = option[1], option[2], option[3]
        popRangeAndInsertPrev(nodes[a], nodes[b], nodes[c])

# 출력
for i in range(1, m + 1):
    printLine(i)