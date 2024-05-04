import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    command = input().split()
    k = command[1]
    if command[0] == 'add':
        dic[k] = command[2]
    elif command[0] == 'remove':
        del dic[k]
    elif command[0] == 'find':
        if k in dic:
            print(dic[k])
        else:
            print('None')