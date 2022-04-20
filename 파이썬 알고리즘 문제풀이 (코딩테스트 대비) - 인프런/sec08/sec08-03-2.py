# 성공
# 1번 문제와 풀이방법 중복

import sys
sys.stdin = open("input.txt", "r")


n = int(input())
memory = [0] * (n+2)
memory[1] = 1
memory[2] = 2
for i in range(3, n+2):
    memory[i] = memory[i-1] + memory[i-2]

print(memory[n+1])