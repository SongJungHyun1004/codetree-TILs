q = int(input())
val = 0
for _ in range(q):
    cmd = input().split()
    if cmd[0] == 'clear':
        val = 0
    else:
        x = int(cmd[1])
        if cmd[0] == 'add':
            val |= (1 << x)
        elif cmd[0] == 'delete':
            if((val >> x) & 1):
                val -= (1 << x)
        elif cmd[0] == 'print':
            print((val >> x) & 1)
        elif cmd[0] == 'toggle':
            val ^= (1 << x)