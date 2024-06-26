q = int(input())
val = 0
for _ in range(q):
    cmd = input().split()
    if len(cmd) == 2:
        x = int(cmd[1])
        if cmd[0] == 'add':
            val = val + (1 << x)
        elif cmd[0] == 'delete':
            val = val - (1 << x)
        elif cmd[0] == 'print':
            print((val >> x) & 1)
        elif cmd[0] == 'toggle':
            val = val ^ (1 << x)
    else:
        val = 0