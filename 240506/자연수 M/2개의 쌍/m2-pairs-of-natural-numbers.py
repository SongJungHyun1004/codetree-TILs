import sys
input = sys.stdin.readline

def solve(N, nums):
    count_dict = {}
    for count, num in nums:
        count_dict[num] = count
        
    sorted_nums = sorted(count_dict.keys())
    min_max_sum = 0
    
    # 가장 작은 수와 가장 큰 수를 짝지어 합을 구함
    while sorted_nums:
        min_num = sorted_nums[0]
        max_num = sorted_nums[-1]
        
        # 두 수를 짝지어서 그 합의 최댓값을 구함
        current_sum = min_num + max_num
        min_max_sum = max(min_max_sum, current_sum)
        
        # 사용된 수의 개수만큼 감소시킴
        used_count = min(count_dict[min_num], count_dict[max_num])
        count_dict[min_num] -= used_count
        if min_num != max_num:
            count_dict[max_num] -= used_count
        
        # 개수가 0이 된 수는 리스트에서 제거
        if count_dict[min_num] == 0:
            sorted_nums.pop(0)
        if sorted_nums and count_dict[max_num] == 0:
            sorted_nums.pop()
            
    return min_max_sum

N = int(input())
nums = []
for _ in range(N):
    cnt, num = map(int, input().split())
    nums.append((cnt, num))

print(solve(N, nums))