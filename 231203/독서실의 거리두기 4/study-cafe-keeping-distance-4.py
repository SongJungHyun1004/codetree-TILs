n = int(input())
study_cafe = list(input())

def get_dist(tmp):
    tmp = tmp.strip('0')
    if '11' in tmp:
        return 1
    x = '101'
    while True:
        if x in tmp:
            return len(x)-1
        x = list(x)
        x.insert(1, '0')
        x = ''.join(x)

mx = float('-inf')
for i in range(n):
    for j in range(i+1, n):
        tmp = study_cafe[:]
        if tmp[i] == '1' or tmp[j] == '1':
            continue
        tmp[i], tmp[j] = '1', '1'
        closest = get_dist(''.join(tmp))
        mx = max(mx, closest)

print(mx)