n, m = map(int, input().split())
num_lst = [i+1 for i in range(n)]
str_lst = [input() for _ in range(n)]
toStr = dict(zip(num_lst, str_lst))
toNum = dict(zip(str_lst, num_lst))
for _ in range(m):
    command = input()
    if command.isdigit():
        print(toStr[int(command)])
    else:
        print(toNum[command])