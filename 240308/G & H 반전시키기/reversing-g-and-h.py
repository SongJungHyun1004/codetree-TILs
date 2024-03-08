n = int(input())
init_string = input()
final_string = input()
cnt = 0
pre = True
if init_string[0] != final_string[0]:
    pre = False
    cnt += 1
for i, j in zip(init_string[1:], final_string[1:]):
    if pre and i != j:
        cnt += 1
        pre = False
    if i==j:
        pre = True
print(cnt)