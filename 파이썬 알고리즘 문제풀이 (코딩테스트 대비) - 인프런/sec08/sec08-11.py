# 실패!
# 풀이시간: 26분

import sys
sys.stdin = open("input.txt", "r")


n, m = map(int, input().split())
quiz = []
for _ in range(n):
    a, b = map(int, input().split())
    quiz.append((a, b))

quiz.sort(key=lambda x:x[1])
memory = [0] * (m+1)

for i in range(n):
    score, time = quiz[i]
    for k in range(time, m+1):
        memory[k] = max(memory[k], memory[k-time]+score)

print(memory[m])