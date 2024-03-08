n = int(input())
init_string = input()
final_string = input()
cnt = 0
length = 0
miss = False
for i in range(n):
    if init_string[i] != final_string[i]:
        length += 1
        if not miss:
            cnt += 1
            miss = True
        if length >= 4:
            length = 0
            miss = False
    else:
        miss = False
print(cnt)