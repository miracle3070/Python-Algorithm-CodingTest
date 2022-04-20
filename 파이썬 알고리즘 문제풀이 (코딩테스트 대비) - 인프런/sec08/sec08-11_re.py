# 성공!
# 풀이시간: 7분

import sys
#sys.stdin = open("input.txt", "r")


n, m = map(int, input().split())
memory = [0] * (m+1)

for _ in range(n):
    score, time = map(int, input().split())
    for k in range(m, time-1, -1):
        memory[k] = max(memory[k], memory[k-time] + score)

print(memory[m])
