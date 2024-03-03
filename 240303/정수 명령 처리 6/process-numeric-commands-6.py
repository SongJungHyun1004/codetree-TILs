import heapq as hq

n = int(input())
max_pq = []
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        hq.heappush(max_pq, -int(command[1]))
    elif command[0] == 'pop':
        rmv = hq.heappop(max_pq)
        print(-rmv)
    elif command[0] == 'size':
        print(len(max_pq))
    elif command[0] == 'empty':
        if max_pq:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        print(-max_pq[0])