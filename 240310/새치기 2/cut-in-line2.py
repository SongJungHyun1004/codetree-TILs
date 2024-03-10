class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = {}

    def find(self, data):
        return self.nodes.get(data, None)

    def pop(self, data):
        node = self.find(data)
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        node.prev = node.next = None

    def append(self, data):
        new_node = Node(data)
        self.nodes[data] = new_node
        if not self.head:
            self.head = self.tail = new_node
            return
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_prev(self, target_data, new_data):
        target_node = self.find(target_data)
        new_node = Node(new_data)
        self.nodes[new_data] = new_node
        if target_node.prev:
            target_node.prev.next = new_node
            new_node.prev = target_node.prev
        new_node.next = target_node
        target_node.prev = new_node
        if target_node == self.head:
            self.head = new_node

    def display(self):
        if not self.head:
            print(-1)
            return
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()
    
    def connect(self, s, e):
        if s:
            s.next = e
        if e:
            e.prev = s
            

# def pop_range_and_insert_prev(s, e, v):
#     # Step 1
#     # s의 이전 노드와 e의 다음 노드를 이어줌
#     connect(s.prev, e.next)

#     # 이제, s의 이전 노드와 e의 다음 노드를 nullptr로 설정
#     s.prev = e.next = None

#     # Step 2
#     # v의 이전 노드와 s를 이어줌
#     connect(v.prev, s)
    
#     # e와 v를 이어줌
#     connect(e, v)

import math
n, m, q = map(int, input().split())
people = list(input().split())
x = n//m
line = [DList() for _ in range(m)]
for i, name in enumerate(people):
    line[i//x].append(name)

for _ in range(q):
    command = input().split()
    if command[0] == '1':
        a, b = command[1], command[2]
        for li in line:
            node_a = li.find(a)
            if node_a:
                li.pop(a)
                break
        for li in line:
            node_b = li.find(b)
            if node_b:
                li.insert_prev(b, a)
        
    elif command[0] == '2':
        a = command[1]
        for li in line:
            node_a = li.find(a)
            if node_a:
                li.pop(a)
                break
    elif command[0] == '3':
        a, b, c = command[1], command[2], command[3]
        for li in line:
            node_a = li.find(a)
            node_b = li.find(b)
            if node_a:
                li.connect(node_a.prev, node_b.next)
                node_a.prev = node_b.next = None
                break
        for li in line:
            node_c = li.find(c)
            if node_c:
                li.connect(node_c.prev, node_a)
                li.connect(node_b, node_c)
                break
for dlst in line:
    dlst.display()