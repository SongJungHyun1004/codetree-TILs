class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_next(cur_node, data):
    data.prev = cur_node
    data.next = cur_node.next

    if data.prev is not None:
        data.prev.next = data
    if data.next is not None:
        data.next.prev = data

def insert_prev(cur_node, data):
    data.prev = cur_node.prev
    data.next = cur_node

    if data.prev is not None:
        data.prev.next = data
    if data.next is not None:
        data.next.prev = data

def pop(cur_node):
    if cur_node.prev is not None:
        cur_node.prev.next = cur_node.next
    if cur_node.next is not None:
        cur_node.next.prev = cur_node.prev

    cur_node.prev = cur_node.next = None

s = input()
cur = Node(s)
n = int(input())
for _ in range(n):
    command = input().split()
    c = int(command[0])
    if c == 1:
        prev = Node(command[1])
        insert_prev(cur, prev)
    elif c == 2:
        next = Node(command[1])
        insert_next(cur, next)
    elif c == 3:
        if cur.prev is not None:
            cur = cur.prev
    elif c == 4:
        if cur.next is not None:
            cur = cur.next

    if cur.prev is None:
        print('(Null)',end=' ')
    else:
        print(cur.prev.data, end=' ')
    print(cur.data, end=' ')
    if cur.next is None:
        print('(Null)')
    else:
        print(cur.next.data)