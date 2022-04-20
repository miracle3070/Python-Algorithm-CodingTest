# 성공!
# 풀이시간: 15분

import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
nums = list(map(int, input().split()))

memory = [0] * (n+1)
nums.insert(0, 0)
memory[1] = 1
result = 0

for i in range(2, n+1):
    max_cnt = 0
    for k in range(i-1, 0, -1):
        if max_cnt < memory[k] and nums[i] > nums[k]:
            max_cnt = memory[k]
    memory[i] = max_cnt + 1
    if result < memory[i]:
        result = memory[i]

print(result)
