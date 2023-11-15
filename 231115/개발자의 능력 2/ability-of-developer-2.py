devs = sorted(list(map(int, input().split())))
mx = max([devs[0]+devs[5], devs[1]+devs[4], devs[2]+devs[3]])
mn = min([devs[0]+devs[5], devs[1]+devs[4], devs[2]+devs[3]])
print(mx-mn)