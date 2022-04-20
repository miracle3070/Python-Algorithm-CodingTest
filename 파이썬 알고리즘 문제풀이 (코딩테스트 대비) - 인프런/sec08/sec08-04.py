# 성공!
# 풀이시간: 19분

import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
nums = list(map(int, input().split()))
memory = []

memory.append((nums[0], 1))

for i in range(1, len(nums)):
    max_cnt = 0
    max_num = -1
    for k in range(len(memory)-1, -1, -1):
        t_num, t_cnt = memory[k]
        if max_cnt < t_cnt and nums[i] > t_num:
            max_num = t_num
            max_cnt = t_cnt
    memory.append((nums[i], max_cnt+1))

result = [x[1] for x in memory]
print(max(result))